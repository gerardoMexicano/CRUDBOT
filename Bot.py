from ast import Call
from email.message import Message
from subprocess import call
from numpy import number
from requests import delete
from sqlalchemy import null
from telegram import Chat, InlineKeyboardMarkup, ReplyMarkup
from telebot import types, TeleBot
from config import * #importamos el token
import telebot # para manejar la API de Telegram
import threading
from telebot.types import ReplyKeyboardMarkup
from telebot.types import ForceReply
from telebot.types import InlineKeyboardButton
from telebot.types import InlineKeyboardMarkup
from telebot.callback_data import CallbackData, CallbackDataFilter
from telebot.custom_filters import AdvancedCustomFilter
bot = telebot.TeleBot(TELEGRAM_TOKEN)

usuarios = {}
llamada=null
funante=null
antemsg=null
antemsg2=null

solicitud = [
    {'id': '0', 'name': 'Asignacion'},
    {'id': '1', 'name': 'objeccion'},
    {'id': '2', 'name': 'Reasignacion'},
    {'id': '3', 'name': 'Liquidacion'}
]
peticioness =[
    {'id': '0','name':'Queja'},
    {'id': '1','name':'Observacion'}
]
dcope =[
    {'id': '0','name':'API'},
    {'id': '1','name':'HUM'},
    {'id': '2','name':'HCH'},
    {'id': '3','name':'MAA'},
    {'id': '4','name':'SMT'},
    {'id': '5','name':'TEC'},
    {'id': '6','name':'TCH'},
    {'id': '7','name':'TLX'},
]
dopc =[
    {'id': '0','name':'NO'},
    {'id': '1','name':'SI'},
]
dsolicitud =[
    {'id': '0','name':'ASIGNACION'},
    {'id': '1','name':'OBJECCION'},
    {'id': '2','name':'REASIGNACION'},
    {'id': '3','name':'LIQUIDACION'},
]
dempresa =[
    {'id': '0','name':'CARSO'},
    {'id': '1','name':'PC INDUSTRIAL'},
    {'id': '2','name':'TEICO'},
]


products_factory = CallbackData('product_id', prefix='products')
factor_selecciones = CallbackData('id_peticion',prefix='peticions')
factor_cope = CallbackData('id_cope',prefix='dcope')
factor_descion =CallbackData('id_opc',prefix='dopc')
factor_solicitud =CallbackData('id_solicitud',prefix='dsolicitud')
factor_empresa =CallbackData('id_empresa',prefix='dempresa')

def products_keyboard():
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text=product['name'],
                    callback_data=products_factory.new(product_id=product["id"])
                )
            ]
            for product in solicitud
        ]
    )


def back_keyboard():
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text='⬅',
                    callback_data='back'
                )
            ]
        ]
    )

#Funciones para un trabaja mas establecido
#funcion para ver como funcionaba
def peticiones1():
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text='Queja',
                    callback_data='queja'
                ),
                types.InlineKeyboardButton(
                    text='Observacion',
                    callback_data='observacion'
                )
            ]
        ]
    )

def peticiones():
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text= peticion['name'],
                    callback_data=factor_selecciones.new(id_peticion=peticion['id'])
                )
                for peticion in peticioness
            
            ]
        ]
    )

def copes():
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text= cop['name'],
                    callback_data=factor_cope.new(id_cope=cop['id'])
                )
                for cop in dcope
            ]
        ]
    )
def solicitu():
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text= fsolicitud['name'],
                    callback_data=factor_solicitud.new(id_solicitud=fsolicitud['id'])
                )
                for fsolicitud in dsolicitud
            ]
        ]
    )
def empre():
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text= fempres['name'],
                    callback_data=factor_empresa.new(id_empresa=fempres['id'])
                )
                for fempres in dempresa
            ]
        ]
    )

def ffopc():
    return types.InlineKeyboardMarkup(
        keyboard=[
            [
                types.InlineKeyboardButton(
                    text= fopc['name'],
                    callback_data=factor_descion.new(id_empresa=fopc['id'])
                )
                for fopc in dopc
            ]
        ]
    )
    

#responde al comando bot 
@bot.message_handler(commands=['help','ayuda'])
def help(message):
    txt='\nAsignacion: use los botones para seleccionar una queja u objeccion'
    txt+='Folio:folio a 8 digitos'
    txt+='\nCope:cope de la solicitud'
    txt+='\nSolicitud: seleccione el servicio'
    txt+='\nEmpresa:Empresa para la que trabaja'
    txt+='\nComentarios Agregue comentarios adicionales\n\n\n\n'
    txt+='\nDeseas relaizar otra solicitud'
    
    bot.send_message(message.chat.id,txt)


@bot.message_handler(commands=['nueva_solicitud','peticion'])
def solicitudes(message):   
    txt='Seleccione una opcion para su nueva peticion'
    global antemsg
    antemsg=message
    global funante
    funante=solicitudes
    bot.send_message(message.chat.id,txt,reply_markup = peticiones())
    
    

@bot.callback_query_handler(func=None, config=factor_selecciones.filter())
def folio(call: types.CallbackQuery):    
    callback_data: dict = factor_selecciones.parse(callback_data=call.data)
    id_peticion = int(callback_data['id_peticion'])
    petici = peticioness [id_peticion]

    text = f": {petici['name']}"
    global antemsg2
    antemsg2=bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=text, reply_markup=back_keyboard())
    antemsg2
    msg=bot.send_message(call.message.chat.id,'Ingresa el folio en digitos')
    antemsg2=call
    global llamada
    llamada=call
    bot.register_next_step_handler(msg,preguntar_cope)

@bot.callback_query_handler(func=None, config=factor_cope.filter())
def cope3(call: types.CallbackQuery):    
    callback_data: dict = factor_cope.parse(callback_data=call.data)
    id_peticion = int(callback_data['id_cope'])
    petici = dcope [id_peticion]

    text = f": {petici['name']}"
    global antemsg2
    antemsg2=bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=text, reply_markup=back_keyboard())
    msg= bot.send_message(call.message.chat.id,"Ingresa la solicitud",reply_markup=solicitu())
    antemsg2=call
    global llamada
    llamada=call

@bot.callback_query_handler(func=None, config=factor_solicitud.filter())
def sempresa(call: types.CallbackQuery):    
    callback_data: dict = factor_solicitud.parse(callback_data=call.data)
    id_peticion = int(callback_data['id_solicitud'])
    petici = dsolicitud [id_peticion]

    text = f": {petici['name']}"
    global antemsg2
    antemsg2=bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=text, reply_markup=back_keyboard())
    msg= bot.send_message(call.message.chat.id,"Ingresa la sempresa",reply_markup=empre())
    antemsg2=call
    global llamada
    llamada=call

@bot.callback_query_handler(func=None, config=factor_empresa.filter())
def scomentario(call: types.CallbackQuery):    
    callback_data: dict = factor_empresa.parse(callback_data=call.data)
    id_peticion = int(callback_data['id_empresa'])
    petici = dempresa [id_peticion]

    text = f": {petici['name']}"
    global antemsg2
    antemsg2=bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=text, reply_markup=back_keyboard())
    msg= bot.send_message(call.message.chat.id,"Ingresa tu comentario")
    antemsg2=call
    global llamada
    llamada=call
    bot.register_next_step_handler(msg,preguntar_comentario)


    

    
def preguntar_cope(message):
    if not message.text.isdigit():
        markup= ForceReply()
        msg= bot.send_message(message.chat.id,'ERROR: DEBES indicar un numero en digitos.\ningresa tu folio',reply_markup=back_keyboard())
        bot.register_next_step_handler(msg,preguntar_cope )
        bot.delete_message(message.chat.id,llamada.message.message_id)
    else:
        """ pregunta el cope de nuesto ususario"""   
        global funante
        funante=folio
        nombre= message.text
        print(nombre)
        markup=copes()
        msg= bot.send_message(message.chat.id,"Ingresa el COPE",reply_markup=markup)


def ejectuar(funcion,llamada):
    funcion(llamada)

@bot.callback_query_handler(func=lambda c: c.data == 'back')
def back_callback(call: types.CallbackQuery):
    bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    bot.clear_step_handler(message=antemsg)
    ejectuar(funante,antemsg)
    
    
    
#funciones de muestra son como un borrador
@bot.message_handler(commands=['servicios'])
def products_command_handler(message):
    bot.send_message(message.chat.id, 'Servicios', reply_markup=products_keyboard())

@bot.callback_query_handler(func=None, config=products_factory.filter())
def products_callback(call: types.CallbackQuery):
    callback_data: dict = products_factory.parse(callback_data=call.data)
    product_id = int(callback_data['product_id'])
    product = solicitud[product_id]

    text = f"Product name: {product['name']}"
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text=text, reply_markup=back_keyboard())

@bot.callback_query_handler(func=lambda c: c.data == 'back1')
def back_callback1(call: types.CallbackQuery):
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                          text="hola")

    
@bot.message_handler(commands=["start"])
def cmd_start(message):
    """Dar bienvenida al usuario del bot"""
    bot.reply_to(message,"bienvenido al bot de la ultima milla")

@bot.message_handler(commands=['alta'])
def cmd_alta(message):
    markup = ForceReply()
    msg = bot.send_message(message.chat.id,"Queja o O.S",reply_markup=markup)
    bot.register_next_step_handler(msg,preguntar_folio)

@bot.message_handler(commands=['alta2'])
def cmd_alta(message):
    markup = ForceReply()
    msg = bot.send_message(message.chat.id,"Queja o O.S",reply_markup=markup)
    bot.register_next_step_handler(msg,preguntar_folio)

def preguntar_folio(message):
    """ pregunta el folio de nuesto ususario"""
    usuarios[message.chat.id]={}
    usuarios[message.chat.id]["peticion"]= message.text
    markup=ForceReply()
    msg= bot.send_message(message.chat.id,"Ingresa el folio",reply_markup=markup)
    bot.register_next_step_handler(msg,preguntar_cope)

def preguntar_cope2(message):
    if not message.text.isdigit():
        markup= ForceReply()
        msg= bot.send_message(message.chat.id,'ERROR: DEBES indicar un numero en digitos.\ningresa tu folio')
        bot.register_next_step_handler(msg,preguntar_cope )
    else:
        """ pregunta el cope de nuesto ususario"""
        nombre= message.text
        print(nombre)
        markup=ForceReply()
        msg= bot.send_message(message.chat.id,"Ingresa el COPE",reply_markup=markup)
        bot.register_next_step_handler(msg,preguntar_solicitud)

def preguntar_solicitud(message):
    """ pregunta el folio de nuesto ususario"""
    nombre= message.text
    print(nombre)
    markup=ForceReply()
    msg= bot.send_message(message.chat.id,"Ingresa la solicitud",reply_markup=markup)
    bot.register_next_step_handler(msg,preguntar_empresa)

def preguntar_empresa(message):
    """ pregunta la empresa de nuesto ususario"""
    nombre= message.text
    print(nombre)
    markup=ForceReply()
    msg= bot.send_message(message.chat.id,"Ingresa la empresa",reply_markup=markup)
    bot.register_next_step_handler(msg,preguntar_comentario)

def preguntar_comentario(message):
    """ pregunta un comentario a nuestro usuario"""
    nombre= message.text
    print(nombre)
    markup=ForceReply()
    msg= bot.send_message(message.chat.id,"Ingresa el comentario",reply_markup=markup)
    bot.register_next_step_handler(msg,Gracias)

def Gracias(message):
    """ nos despedimos del usuario"""
    comentario= message.text
    print(comentario)
    bot.send_message(message.chat.id,"Gracias tu solicitud ha sido enviada")

@bot.message_handler(commands=['cope'])
def cmd_cope(message):
    markup= InlineKeyboardMarkup(row_width = 2)
    b1=InlineKeyboardButton("API",callback_data='API')
    b2=InlineKeyboardButton("HUM",callback_data='HUM')
    b3=InlineKeyboardButton("HVH",callback_data='HCH')
    b4=InlineKeyboardButton("MAA",callback_data='MAA')
    b5=InlineKeyboardButton("SMT",callback_data='SMT')
    b6=InlineKeyboardButton("TEC",callback_data='TEC')
    b7=InlineKeyboardButton("TEH",callback_data='TEH')
    b8=InlineKeyboardButton("TLX",callback_data='TLX')
    markup.add(b1,b2,b3,b4,b5,b6,b7,b8)
    bot.send_message(message.chat.id,"selecciona COPE",reply_markup=markup)
    

class ProductsCallbackFilter(AdvancedCustomFilter):
    key = 'config'

    def check(self, call: types.CallbackQuery, config: CallbackDataFilter):
        return config.check(query=call)

def recibir_mensajes(timer_runs):
    while timer_runs.is_set():
        print('Iniciando el bot')
        bot.add_custom_filter(ProductsCallbackFilter())
        bot.infinity_polling()
        print('fin')

def iniciarbot():
    hilo_bot = threading.Thread(name="hilo_bot",target=recibir_mensajes)
    hilo_bot.start()
def detener():
    bot.stop_bot()

# MAIN ####################################################
if __name__ == '__main__':
    print('Iniciando el bot')
    bot.add_custom_filter(ProductsCallbackFilter())
    bot.infinity_polling()
    bot.stop_bot()
    print('fin')