# Discord chat vocale e testuale - https://discordapp.com/
wget -O discord.dmg https://discordapp.com/api/download?platform=osx
hdiutil mount discord.dmg
cd /Volumes/Discord
sudo cp -R Discord.app /Applications/Discord.app/
hdiutil unmount /Volumes/Discord
cd ~/YAPI
rm scripts/discord.dmg
