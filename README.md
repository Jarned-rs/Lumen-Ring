# Lumen-Ring

The lumen ring is a simple project designed to teach myself about charlieplexing and how it works in real situations. It reacts on the volume that your PC is set to and has a OLED to show upcoming events for you that can be changed easily in the code.

# Features
- RP2040-Zero to control the LEDS and OLED
- OLED to display your upcoming events
- 20 LEDS charlieplexed in 5pin with 3 colours to correspond with your PC's volume
- A rotary encoder to turn your volume up, down and mute sound
- A case with a hinge to keep the LEDs and OLED safe during storage! 

# How it works
On a basic GPIO port, we have 2 main modes that they can be in, either HIGH or LOW. Charlieplexing uses a 3rd mode called INPUT to fit more LEDS on one pin.
- A script reads the volume and sends it via USB to the 2040
- The 2040 reads the volume and decides how many LEDS need to be switched on
- It finds the right LEDs and turns them on

# Photos
Case:
<img width="1734" height="1087" alt="image" src="https://github.com/user-attachments/assets/3e24c82c-5935-48ac-8b14-49a1d19b2c40" />
Schematic:
<img width="926" height="824" alt="image" src="https://github.com/user-attachments/assets/3380ec48-67ae-42b3-8cf0-f9dcbc00c406" />
PCB:
<img width="1396" height="747" alt="image" src="https://github.com/user-attachments/assets/6ea77a98-653e-4cc7-95b9-79d77b2fe563" />

BOM:
|Part|QTY|Price|Link|Note|
|----------|---------|-----|-------------|--------|
|RP2040-Zero|1|0|N/A|Already Owned|
|LEDs|20|$1.35|https://www.aliexpress.com/item/1005004966964656.html?spm=a2g0o.detail.0.0.72c7Vs5tVs5tkD&mp=1||
|Resistors|5|$5.55|https://www.aliexpress.com/item/1005011772534173.html?spm=a2g0o.cart.0.0.778838daPJe0Vl&mp=1||
|0.96" OLED|1|$2.23|https://www.aliexpress.com/item/1005006827999782.html?spm=a2g0o.cart.0.0.6f1e38daj4PjJx&mp=1||
|Case|1|$5|N/A|Friend is printing for me|

Total = $14.14
