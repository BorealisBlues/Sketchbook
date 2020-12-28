const Discord = require('discord.js');
 const client = new Discord.Client();

client.on("ready", () =>{
    console.log(`Logged in as ${client.user.tag}!`);
    client.user.setPresence({
        status: "online",  //You can show online, idle....
        game: {
            name: "Using !help",  //The message shown
            type: "STREAMING" //PLAYING: WATCHING: LISTENING: STREAMING:
        }
    });
 });

client.on('message', msg => {
 if (msg.content === 'ping') {
 msg.reply('pong');
 client.user.setPresence({
  status: "online",  //You can show online, idle....
  game: {
   name: "Using !help",  //The message shown
   type: "STREAMING" //PLAYING: WATCHING: LISTENING: STREAMING:
        }
    })
 }
 });

client.login('NzI1ODg0NDgyMzA5MTkzNzUw.XvVOpA.BngU6LWAu7HLF-B1ODmn_Bo9Isg');