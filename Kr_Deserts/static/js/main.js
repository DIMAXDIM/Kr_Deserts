//
// import * as aaa from './telebot'


console.log('dasfdsfsdfasfsa')
console.log('dasfdsfsdfasfsa')
console.log('dasfdsfsdfasfsa')
console.log('dasfdsfsdfasfsa')
const TELEGRAM_BOT_TOKEN = ''



// var TeleBot = require('telebot');

// const TeleBot = require('telebot');
import * as TeleBot from './telebot';



const bot = new TeleBot(TELEGRAM_BOT_TOKEN);Timeout: 5000 // Reconnecting timeout (in ms)





bot.on(['/start', '/help'], function(msg) {
    return bot.sendMessage(msg.from.id, 'Bam!');

  });

bot.connect()