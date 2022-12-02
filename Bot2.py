from config import * #importamos el token
from databasebot import Databot
import threading
import telebot # para manejar la API de Telegram
from telebot.types import InlineKeyboardMarkup # crear botonera
from telebot.types import InlineKeyboardButton
from telebot.callback_data import CallbackData, CallbackDataFilter
from telebot.custom_filters import AdvancedCustomFilter
from telebot import types
from telebot.types import ForceReply


bot = telebot.TeleBot(TELEGRAM_TOKEN)#se crea el bot

datos=Databot()

#variables
usuarios={}
antemsg=None
llamada=None

#factory
factor_selecciones = CallbackData('alta_id', prefix='alta')
factor_copes = CallbackData('cope_id', prefix='cope')
factor_solicitud=CallbackData('solicitud_id',prefix='solicitud')
factor_empresa=CallbackData('empresa_id',prefix='empresa')
#comandos

#se agrega una funcion oyente que espera especifiacamente una de los comandos 
#se concatena con información
@bot.message_handler(commands=['help','ayuda'])
def help(message):
    txt='\n Escriba "/petición" para iniciar una nueva solicitud'
    txt+='\nAsignacion: use los botones para seleccionar una queja u objeccion'
    txt+='\nFolio:folio a 8 digitos'
    txt+='\nCope:cope de la solicitud'
    txt+='\nSolicitud: seleccione el servicio'
    txt+='\nEmpresa:Empresa para la que trabaja'
    txt+='\nComentarios Agregue comentarios adicionales\n\n\n\n'
    txt+='\nDeseas relaizar otra solicitud'
    
    bot.reply_to(message,txt)

#esta funcion genera las nuevas solicitudes de empleados
@bot.message_handler(commands=['nueva_solicitud','peticion','petición'])
def solicitudes(message):   
    txt='Seleccione una opción para su nueva petición'
    global antemsg
    antemsg=message
    markup= InlineKeyboardMarkup(row_width=5)
    consulta=Databot().returtALLAltas()
    num=len(consulta)
    y=0
    while y <num:
        if ((y+4)<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_selecciones.new(alta_id= consulta[y][0]))
            B2=InlineKeyboardButton(consulta[y+1][2],callback_data=factor_selecciones.new(alta_id=consulta[y+1][0]))
            B3=InlineKeyboardButton(consulta[y+2][2],callback_data=factor_selecciones.new(alta_id=consulta[y+2][0]))
            B4=InlineKeyboardButton(consulta[y+3][2],callback_data=factor_selecciones.new(alta_id=consulta[y+3][0]))
            B5=InlineKeyboardButton(consulta[y+4][2],callback_data=factor_selecciones.new(alta_id=consulta[y+4][0]))
            markup.add(B1,B2,B3,B4,B5)
            y+=5
        elif ((y+3)<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_selecciones.new(alta_id=consulta[y][0]))
            B2=InlineKeyboardButton(consulta[y+1][2],callback_data=factor_selecciones.new(alta_id=consulta[y+1][0]))
            B3=InlineKeyboardButton(consulta[y+2][2],callback_data=factor_selecciones.new(alta_id=consulta[y+2][0]))
            B4=InlineKeyboardButton(consulta[y+3][2],callback_data=factor_selecciones.new(alta_id=consulta[y+3][0]))
            markup.add(B1,B2,B3,B4)
            y+=4
        elif ((y+2)<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_selecciones.new(alta_id=consulta[y][0]))
            B2=InlineKeyboardButton(consulta[y+1][2],callback_data=factor_selecciones.new(alta_id=consulta[y+1][0]))
            B3=InlineKeyboardButton(consulta[y+2][2],callback_data=factor_selecciones.new(alta_id=consulta[y+2][0]))
            markup.add(B1,B2,B3)
            y+=3
        elif ((y+1)<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_selecciones.new(alta_id=consulta[y][0]))
            B2=InlineKeyboardButton(consulta[y+1][2],callback_data=factor_selecciones.new(alta_id=consulta[y+1][0]))
            markup.add(B1,B2)
            y+=2
        elif (y<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_selecciones.new(alta_id=consulta[y][0]))
            markup.add(B1)
   
    bot.send_message(message.chat.id,txt,reply_markup=markup)

@bot.callback_query_handler(func=None, config=factor_selecciones.filter())
def folio(call: types.CallbackQuery):
    callback_data: dict = factor_selecciones.parse(callback_data=call.data)
    alta_id= int(callback_data['alta_id'])
    consulta=Databot().returtALLAltas()
    num=len(consulta)
    alta=''
    for x in range(num):
         if (consulta[x][0]==alta_id):
            alta=consulta[x][1]
            break
    text=alta
    usuarios[call.message.chat.id]={}
    usuarios[call.message.chat.id]["alta"]=text
    bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=text)
    msg=bot.send_message(call.message.chat.id,text='Ingresa el folio en digitos')
    global llamada
    llamada=call
    bot.register_next_step_handler(msg,preguntar_cope)


def preguntar_cope(message):
    if not message.text.isdigit():
        markup= ForceReply()
        msg= bot.send_message(message.chat.id,'ERROR: DEBES indicar un numero en digitos.\ningresa tu folio',reply_markup=markup)
        bot.register_next_step_handler(msg,preguntar_cope)
        bot.delete_message(message.chat.id,llamada.message.message_id)  
    else:
        """ pregunta el cope de nuesto ususario""" 
        global antemsg
        antemsg=message  
        consultas=Databot().returtALLcopes()
        markup=copes(consultas)
        usuarios[message.chat.id]["folio"]=message.text
        bot.send_message(message.chat.id,"Ingresa el COPE",reply_markup=markup)  

@bot.callback_query_handler(func=None,config=factor_copes.filter())
def cope(call:types.CallbackQuery):
    callback_data: dict = factor_copes.parse(callback_data=call.data)
    cope_id=int(callback_data['cope_id'])
    consulta=Databot().returtALLcopes()
    num=len(consulta)
    icope=''
    for x in range(num):
         if (consulta[x][0]==cope_id):
            icope=consulta[x][1]
            break
    text=icope
    usuarios[call.message.chat.id]["cope"]=text
    consultas=Databot().returtALLsolicitudes()
    markup=solicitud(consultas)
    bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=text)
    bot.send_message(call.message.chat.id,text="Ingresa la solicitud",reply_markup=markup)

@bot.callback_query_handler(func=None,config=factor_solicitud.filter())
def sempresa(call:types.CallbackQuery):
    callback_data: dict = factor_solicitud.parse(callback_data=call.data)
    solicitud_id=int(callback_data['solicitud_id'])
    consulta=Databot().returtALLsolicitudes()
    num=len(consulta)
    isolicitud=''
    for x in range(num):
         if (consulta[x][0]==solicitud_id):
            isolicitud=consulta[x][1]
            break
    text=isolicitud
    usuarios[call.message.chat.id]["solicitud"]=text
    consultas=Databot().returtALLempresas()
    markup=empresa(consultas)
    bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=text)
    bot.send_message(call.message.chat.id,text="Ingresa la Empresa",reply_markup=markup)

@bot.callback_query_handler(func=None,config=factor_empresa.filter())
def scomentario(call:types.CallbackQuery):
    callback_data: dict = factor_empresa.parse(callback_data=call.data)
    empresa_id=int(callback_data['empresa_id'])
    consulta=Databot().returtALLempresas()
    num=len(consulta)
    iempresa=''
    for x in range(num):
         if (consulta[x][0]==empresa_id):
            iempresa=consulta[x][1]
            break
    text=iempresa
    usuarios[call.message.chat.id]["empresa"]=text
    bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=text)
    msg=bot.send_message(call.message.chat.id,text='Ingresa tu comentario')
    global llamada
    llamada=call
    bot.register_next_step_handler(msg,verificacion)

def verificacion(message):
    global antemsg
    antemsg=message 
    
    markup=InlineKeyboardMarkup()
    b1=InlineKeyboardButton("SI",callback_data="enviar")
    b2=InlineKeyboardButton("CANCELAR",callback_data="cancelar")
    markup.add(b1,b2)
    usuarios[message.chat.id]["comentario"]=message.text
    texto='Datos Registrados:\n'
    texto+=f'<code>ALTA......:</code>{usuarios[message.chat.id]["alta"]}\n'
    texto+=f'<code>FOLIO.....:</code>{usuarios[message.chat.id]["folio"]}\n'
    texto+=f'<code>COPE......:</code>{usuarios[message.chat.id]["cope"]}\n'
    texto+=f'<code>SOLICITUD.:</code>{usuarios[message.chat.id]["solicitud"]}\n'
    texto+=f'<code>EMPRESA...:</code>{usuarios[message.chat.id]["empresa"]}\n'
    texto+=f'<code>COMENTARIO:</code>{usuarios[message.chat.id]["comentario"]}\n'
    texto+=f'Verifica que tus datos sean correctos'
    bot.send_message(message.chat.id,text=texto,parse_mode="html",reply_markup=markup)
@bot.callback_query_handler(func=lambda x:True)
def respuesta_envios(call):
    cid=call.from_user.id
    mid=call.message.chat.id
    if call.data == "enviar":
        
        valta=str(usuarios[call.message.chat.id]["alta"])
        vfolios=usuarios[call.message.chat.id]["folio"]
        vcopes=usuarios[call.message.chat.id]["cope"]
        vsolicitud=usuarios[call.message.chat.id]["solicitud"]
        vempresa=usuarios[call.message.chat.id]["empresa"]
        vcomen=str(usuarios[call.message.chat.id]["comentario"])
        texto='Datos Registrados:\n'
        texto+=f'<code>ALTA......:</code>{usuarios[call.message.chat.id]["alta"]}\n'
        texto+=f'<code>FOLIO.....:</code>{usuarios[call.message.chat.id]["folio"]}\n'
        texto+=f'<code>COPE......:</code>{usuarios[call.message.chat.id]["cope"]}\n'
        texto+=f'<code>SOLICITUD.:</code>{usuarios[call.message.chat.id]["solicitud"]}\n'
        texto+=f'<code>EMPRESA...:</code>{usuarios[call.message.chat.id]["empresa"]}\n'
        texto+=f'<code>COMENTARIO:</code>{usuarios[call.message.chat.id]["comentario"]}\n'
        texto+=f'Verifica que tus datos sean correctos'
        Databot().insertclientes(mid,valta,vfolios,vcopes,vsolicitud,vempresa,vcomen)
        Databot().insertclientes2(mid,valta,vfolios,vcopes,vsolicitud,vempresa,vcomen)
        del usuarios[call.message.chat.id]
        txt="Gracias Tu solicitud ha sido enviada\n"
        txt+="si deseas una nueva solicitud presiona\n"
        txt+=""
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,parse_mode="html",text=texto)
        bot.send_message(call.message.chat.id,txt)
    if call.data=="cancelar":
        texto="se ha cancelado"
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text=texto)
        bot.send_message(call.message.chat.id,txt)




    
#markups
def copes(consulta):
    num=len(consulta)
    markup= InlineKeyboardMarkup(row_width=5)
    y=0
    while (y <num):
        if ((y+4)<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_copes.new(cope_id= consulta[y][0]))
            B2=InlineKeyboardButton(consulta[y+1][2],callback_data=factor_copes.new(cope_id=consulta[y+1][0]))
            B3=InlineKeyboardButton(consulta[y+2][2],callback_data=factor_copes.new(cope_id=consulta[y+2][0]))
            B4=InlineKeyboardButton(consulta[y+3][2],callback_data=factor_copes.new(cope_id=consulta[y+3][0]))
            B5=InlineKeyboardButton(consulta[y+4][2],callback_data=factor_copes.new(cope_id=consulta[y+4][0]))
            markup.add(B1,B2,B3,B4,B5)
            y+=5
        elif ((y+3)<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_copes.new(cope_id=consulta[y][0]))
            B2=InlineKeyboardButton(consulta[y+1][2],callback_data=factor_copes.new(cope_id=consulta[y+1][0]))
            B3=InlineKeyboardButton(consulta[y+2][2],callback_data=factor_copes.new(cope_id=consulta[y+2][0]))
            B4=InlineKeyboardButton(consulta[y+3][2],callback_data=factor_copes.new(cope_id=consulta[y+3][0]))
            markup.add(B1,B2,B3,B4)
            y+=4
        elif ((y+2)<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_copes.new(cope_id=consulta[y][0]))
            B2=InlineKeyboardButton(consulta[y+1][2],callback_data=factor_copes.new(cope_id=consulta[y+1][0]))
            B3=InlineKeyboardButton(consulta[y+2][2],callback_data=factor_copes.new(cope_id=consulta[y+2][0]))
            markup.add(B1,B2,B3)
            y+=3
        elif ((y+1)<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_copes.new(cope_id=consulta[y][0]))
            B2=InlineKeyboardButton(consulta[y+1][2],callback_data=factor_copes.new(cope_id=consulta[y+1][0]))
            markup.add(B1,B2)
            y+=2
        elif (y<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_copes.new(cope_id=consulta[y][0]))
            markup.add(B1)
    return markup
def solicitud(consulta):
    num=len(consulta)
    markup= InlineKeyboardMarkup(row_width=5)
    y=0
    while (y <num):
        if ((y+4)<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_solicitud.new(solicitud_id= consulta[y][0]))
            B2=InlineKeyboardButton(consulta[y+1][2],callback_data=factor_solicitud.new(solicitud_id=consulta[y+1][0]))
            B3=InlineKeyboardButton(consulta[y+2][2],callback_data=factor_solicitud.new(solicitud_id=consulta[y+2][0]))
            B4=InlineKeyboardButton(consulta[y+3][2],callback_data=factor_solicitud.new(solicitud_id=consulta[y+3][0]))
            B5=InlineKeyboardButton(consulta[y+4][2],callback_data=factor_solicitud.new(solicitud_id=consulta[y+4][0]))
            markup.add(B1,B2,B3,B4,B5)
            y+=5
        elif ((y+3)<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_solicitud.new(solicitud_id=consulta[y][0]))
            B2=InlineKeyboardButton(consulta[y+1][2],callback_data=factor_solicitud.new(solicitud_id=consulta[y+1][0]))
            B3=InlineKeyboardButton(consulta[y+2][2],callback_data=factor_solicitud.new(solicitud_id=consulta[y+2][0]))
            B4=InlineKeyboardButton(consulta[y+3][2],callback_data=factor_solicitud.new(solicitud_id=consulta[y+3][0]))
            markup.add(B1,B2,B3,B4)
            y+=4
        elif ((y+2)<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_solicitud.new(solicitud_id=consulta[y][0]))
            B2=InlineKeyboardButton(consulta[y+1][2],callback_data=factor_solicitud.new(solicitud_id=consulta[y+1][0]))
            B3=InlineKeyboardButton(consulta[y+2][2],callback_data=factor_solicitud.new(solicitud_id=consulta[y+2][0]))
            markup.add(B1,B2,B3)
            y+=3
        elif ((y+1)<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_solicitud.new(solicitud_id=consulta[y][0]))
            B2=InlineKeyboardButton(consulta[y+1][2],callback_data=factor_solicitud.new(solicitud_id=consulta[y+1][0]))
            markup.add(B1,B2)
            y+=2
        elif (y<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_solicitud.new(solicitud_id=consulta[y][0]))
            markup.add(B1)
    return markup
def empresa(consulta):
    num=len(consulta)
    markup= InlineKeyboardMarkup(row_width=5)
    y=0
    while (y <num):
        if ((y+4)<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_empresa.new(empresa_id= consulta[y][0]))
            B2=InlineKeyboardButton(consulta[y+1][2],callback_data=factor_empresa.new(empresa_id=consulta[y+1][0]))
            B3=InlineKeyboardButton(consulta[y+2][2],callback_data=factor_empresa.new(empresa_id=consulta[y+2][0]))
            B4=InlineKeyboardButton(consulta[y+3][2],callback_data=factor_empresa.new(empresa_id=consulta[y+3][0]))
            B5=InlineKeyboardButton(consulta[y+4][2],callback_data=factor_empresa.new(empresa_id=consulta[y+4][0]))
            markup.add(B1,B2,B3,B4,B5)
            y+=5
        elif ((y+3)<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_empresa.new(empresa_id=consulta[y][0]))
            B2=InlineKeyboardButton(consulta[y+1][2],callback_data=factor_empresa.new(empresa_id=consulta[y+1][0]))
            B3=InlineKeyboardButton(consulta[y+2][2],callback_data=factor_empresa.new(empresa_id=consulta[y+2][0]))
            B4=InlineKeyboardButton(consulta[y+3][2],callback_data=factor_empresa.new(empresa_id=consulta[y+3][0]))
            markup.add(B1,B2,B3,B4)
            y+=4
        elif ((y+2)<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_empresa.new(empresa_id=consulta[y][0]))
            B2=InlineKeyboardButton(consulta[y+1][2],callback_data=factor_empresa.new(empresa_id=consulta[y+1][0]))
            B3=InlineKeyboardButton(consulta[y+2][2],callback_data=factor_empresa.new(empresa_id=consulta[y+2][0]))
            markup.add(B1,B2,B3)
            y+=3
        elif ((y+1)<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_empresa.new(empresa_id=consulta[y][0]))
            B2=InlineKeyboardButton(consulta[y+1][2],callback_data=factor_empresa.new(empresa_id=consulta[y+1][0]))
            markup.add(B1,B2)
            y+=2
        elif (y<num):
            B1=InlineKeyboardButton(consulta[y][2],callback_data=factor_empresa.new(empresa_id=consulta[y][0]))
            markup.add(B1)
    return markup
        
"""
@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id,"Comando no disponible")
    else:
        txt='\nUn gusto soy el bot de la ultima milla estoy aqui para ayudarte '
        txt+='\nEscriba "/help" para intrucciones'
        txt+='\nEscriba "/petición" para iniciar una nueva solicitud'
        
       
        bot.send_message(message.chat.id,txt)
        """
#mensajes
def mensaje(chat_id,mensaje):
    bot.send_message(chat_id=chat_id,text=mensaje)
class ProductsCallbackFilter(AdvancedCustomFilter):
    key = 'config'

    def check(self, call: types.CallbackQuery, config: CallbackDataFilter):
        return config.check(query=call)

def recibir_mensajes():
        print('Iniciando el bot')
        bot.add_custom_filter(ProductsCallbackFilter())
        bot.infinity_polling()
        print('fin')

def iniciarbot():
    hilo_bot = threading.Thread(name="hilo_bot",target=recibir_mensajes)
    hilo_bot.start()
def detener():
    bot.stop_bot()

if __name__ == '__main__':
    print('Iniciando el bot')
    #bot.add_custom_filter(ProductsCallbackFilter())
    #bot.infinity_polling()
    print('fin')