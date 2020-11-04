import discord
from discord.ext import commands

client = commands.Bot(command_prefix=',')
@client.remove_command('help')

@client.event
async def on_ready():
	print('I working.')
	await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.playing, name='Если нужна помощь: ,help'))

#help
@client.command()
async def help(ctx):
	author = ctx.message.author
	e = discord.Embed(title = 'Помощь', description = 'help (Показать этот список)\nclear (Очистка сообщений)\nmute (Заглушить человека)\nunmute(Разглушить человека)', color = discord.Color.dark_green())
	e.set_footer(text=f'Called By {author}', icon_url=ctx.author.avatar_url)
	await ctx.send(embed=e)

#ban
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, m: discord.Member):
	a = ctx.message.author
	e = discord.Embed(title='Пользователь забанен', description = f'Пользователь: {m} был забанен!')
	await m.ban()
	await ctx.send(embed=e)

#unban
@client.command()
async def unban(ctx, *, m):
	ub=await ctx.guild.bans()
	for ban_entry in ub:
		user=ban_entry.user
		r = 1

#clear
@client.command()
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=0):
 	author = ctx.message.author
 	er = discord.Embed(title='Ошибка', description = f'Простите {author.mention}, но к сожелению я не могу удалить {amount} сообщений!', color = discord.Color.red())
 	e = discord.Embed(description=f'Удалено сообщений: {amount}', color = discord.Color.blue(), title='Очистка')
 	e.set_footer(text=f'Админ: {author}', icon_url=ctx.author.avatar_url)
 	e.set_thumbnail(url='http://pngimg.com/uploads/trash_can/trash_can_PNG18476.png')
 	if amount != 0:
 	 await ctx.channel.purge(limit=1)
 	 await ctx.channel.purge(limit = amount)
 	 await ctx.send(embed=e)
 	else: await ctx.send(embed=er), print(f'[Admin System] {author} попытался отчистить 0 сообщений. Ошибка выдана.')

#mute
@client.command()
@commands.has_permissions(manage_messages = True)
async def mute(ctx, member: discord.Member, reason):
	author = ctx.message.author
	role = discord.utils.get(ctx.guild.roles, name="mute")
	e = discord.Embed(title='Пользователь замучен!', description=f'Пользователь: {member.mention} был замучен.\nПричина: {reason}', color = discord.Color.green())
	e.set_footer(text=f'Админ: {author}', icon_url=ctx.author.avatar_url)
	e.set_thumbnail(url='https://www.freepng.ru/png-ig0jax.html')
	await member.add_roles(role)
	await ctx.send(embed=e)

#unmute
@client.command()
@commands.has_permissions(manage_messages = True)
async def unmute(ctx, member: discord.Member):
	author = ctx.message.author
	role = discord.utils.get(ctx.guild.roles, name="mute")
	e=discord.Embed(title='Пользователь размучен!', description=f'Пользователь: {member.mention} больше не в муте.')
	e.set_footer(text=f"Админ: {author}", icon_url=ctx.author.avatar_url)
	await member.remove_roles(role)
	await ctx.send(embed=e)
	await member.send(embed=discord.Embed(
	title = 'Вы были размьючены!',
	description = f'Администратор: {author}',
	color = discord.Color.green()))

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		e = discord.Embed(
		title = 'Вампус не смог найти у меня эту команду.',
		color = discord.Color.red())
		await ctx.send(embed=e)
	if isinstance(error, commands.MissingPermissions):
		e = discord.Embed(
		title = 'Прости но я не могу дать тебе этого сделать, возвращайся когда станешь эм... покруче!',
		color = discord.Color.red())
		await ctx.send(embed=e)
	if isinstance(error, commands.BadArgument):
		e = discord.Embed(
		title = 'Эм... ты уверен что этим я могу выполнить команду?',
		color = discord.Color.red())
		await ctx.send(embed=e)
	if isinstance(error, commands.MissingRequiredArgument):
		e = discord.Embed(
		title = 'Видимо вы пропустили аргумент!',
		color = discord.Color.red())
		await ctx.send(embed=e)

client.run(NzY0Nzc2NjE2NTA4OTE1NzEy.X4LLug.XrZZjH0oZMt9dSmRCEU-ccSudnk)
