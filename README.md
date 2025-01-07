<a href="https://www.buymeacoffee.com/0xDTC"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a knowledge&emoji=📖&slug=0xDTC&button_colour=FF5F5F&font_colour=ffffff&font_family=Comic&outline_colour=000000&coffee_colour=FFDD00" /></a>

# Docker + kali usage

```bash
# Build simple kali image with mounted /kali dir
docker-compose build

# Run default script within container (Autoscan.sh)
docker-compose run kali

# Run a raw bash within kali container
docker-compose run kali bash
```
