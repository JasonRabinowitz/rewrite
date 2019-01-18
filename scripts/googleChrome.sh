# Google Chrome Browser - https://www.google.com/chrome/
wget -O chrome.dmg https://dl.google.com/chrome/mac/stable/GGRO/googlechrome.dmg
hdiutil mount chrome.dmg
cd "/Volumes/Google Chrome"
cp "Google Chrome.app" "/Applications/Google Chrome.app"
hdiutil unmount "/Volumes/Google Chrome"
cd ~/YAPI
rm scripts/chrome.dmg
