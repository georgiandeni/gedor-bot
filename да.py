import discord
from discord.ext import commands

botguild = commands.Bot.get_guild(self, id=671299130907426816) #доделать

botacc = botguild.get_member(user_id=581506941361192960)

print(botacc)

bot = commands.Bot(command_prefix='*')

discord.Guild.troles=['0', 0]

@bot.command()
async def t_role(ctx, triggerroleid, givenroleid):
    ctx.message.guild.troles[0]=str(triggerroleid)
    ctx.message.guild.troles[1]=int(givenroleid)
    
@bot.event
async def on_ready():
        print('Logged on!')

@bot.command()
async def sum(ctx, arg1, arg2):
    sum_output = int(arg1) + int(arg2)
    await ctx.send(sum_output)

@bot.event
async def on_member_update(before, after):
    if before.roles != after.roles:
        print(before.guild.troles[0])
        for rolecheck in range (len(after.roles)):
            if str(after.roles[rolecheck].id) == before.guild.troles[0]:
                role = before.guild.get_role(role_id=before.guild.troles[1])
                await before.add_roles(role, reason='Trigger role', atomic=True)

bot.run('NTgxNTA2OTQxMzYxMTkyOTYw.XnRozg.BEZhxB9vH2eIdIfUln9D0N2Wxn4')
