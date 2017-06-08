EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:rc-video
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Schematic for sensor unit and main unit"
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L raspberry_pi_zero U?
U 1 1 59391A10
P 2600 3150
F 0 "U?" H 1200 2500 60  0001 C CNN
F 1 "raspberry_pi_zero" H 2350 2950 60  0000 C CNN
F 2 "" H 2350 2950 60  0000 C CNN
F 3 "" H 2350 2950 60  0000 C CNN
	1    2600 3150
	1    0    0    -1  
$EndComp
$Comp
L S7V8F5 U?
U 1 1 59391B77
P 8250 1650
F 0 "U?" H 8300 1700 60  0001 C CNN
F 1 "S7V8F5" H 8250 1650 60  0000 C CNN
F 2 "" H 8250 1650 60  0000 C CNN
F 3 "" H 8250 1650 60  0000 C CNN
	1    8250 1650
	1    0    0    -1  
$EndComp
$Comp
L 74HCT245AP U?
U 1 1 59393B32
P 8250 4650
F 0 "U?" H 8250 4650 60  0001 C CNN
F 1 "74HCT245AP" H 8250 4650 60  0000 C CNN
F 2 "" H 8250 4650 60  0000 C CNN
F 3 "" H 8250 4650 60  0000 C CNN
	1    8250 4650
	1    0    0    -1  
$EndComp
$Comp
L US1881 U?
U 1 1 59393DEC
P 5250 5500
F 0 "U?" H 5250 5500 60  0001 C CNN
F 1 "US1881" H 5250 5400 60  0000 C CNN
F 2 "" H 5250 5500 60  0000 C CNN
F 3 "" H 5250 5500 60  0000 C CNN
	1    5250 5500
	1    0    0    -1  
$EndComp
$Comp
L Teensy_LC U?
U 1 1 59393E00
P 5350 1700
F 0 "U?" H 5350 1700 60  0001 C CNN
F 1 "Teensy_LC" H 5350 1700 60  0000 C CNN
F 2 "" H 5350 1700 60  0000 C CNN
F 3 "" H 5350 1700 60  0000 C CNN
	1    5350 1700
	1    0    0    -1  
$EndComp
Text Notes 10650 2700 0    60   ~ 0
RX 6V
Text Notes 10650 2900 0    60   ~ 0
RX GND
Text Notes 10650 3200 0    60   ~ 0
RX Throttle\nSignal
Text Notes 10650 3450 0    60   ~ 0
RX Steering\nSignal
Connection ~ 10550 2700
Connection ~ 10550 2900
Connection ~ 10550 3100
Wire Wire Line
	8350 2700 8350 2250
Wire Wire Line
	8200 2900 8200 2250
Connection ~ 8200 2900
Wire Wire Line
	8850 3800 9350 3800
Wire Wire Line
	9350 2900 9350 6350
Connection ~ 9350 2900
Wire Wire Line
	9350 6350 7650 6350
Wire Wire Line
	7650 6350 7650 5850
Connection ~ 9350 3800
Wire Wire Line
	8850 3050 8850 3600
Wire Wire Line
	5750 2900 5750 2200
Wire Wire Line
	8050 2250 8050 2750
Wire Wire Line
	8050 2750 5900 2750
Wire Wire Line
	5900 2750 5900 2200
Wire Wire Line
	5600 2200 5600 3800
Wire Wire Line
	5600 3050 8850 3050
Connection ~ 10550 3350
Wire Wire Line
	10550 2700 8350 2700
Wire Wire Line
	5750 2900 10550 2900
Wire Wire Line
	10550 3100 10000 3100
Wire Wire Line
	8850 4000 10000 4000
Wire Wire Line
	10000 4000 10000 3100
Wire Wire Line
	10550 3350 10200 3350
Wire Wire Line
	10200 3350 10200 4200
Wire Wire Line
	10200 4200 8850 4200
Wire Wire Line
	7650 3600 7650 2900
Connection ~ 7650 2900
Wire Wire Line
	7650 3800 7500 3800
Wire Wire Line
	7500 3800 7500 3200
Wire Wire Line
	7500 3200 5300 3200
Wire Wire Line
	5300 3200 5300 2200
Wire Wire Line
	7650 4000 7350 4000
Wire Wire Line
	7350 4000 7350 3350
Wire Wire Line
	7350 3350 5150 3350
Wire Wire Line
	5150 3350 5150 2200
Wire Wire Line
	5450 2200 5450 5000
Wire Wire Line
	5250 5000 5250 4100
Wire Wire Line
	3350 4100 6450 4100
Wire Wire Line
	6450 4100 6450 2900
Connection ~ 6450 2900
Connection ~ 5250 4100
Wire Wire Line
	5600 3800 5050 3800
Wire Wire Line
	5050 3800 5050 5000
Connection ~ 5600 3050
Wire Wire Line
	6650 2750 6650 4300
Wire Wire Line
	6650 4300 3250 4300
Wire Wire Line
	3250 4300 3250 4100
Connection ~ 6650 2750
Wire Wire Line
	3050 4500 3050 4100
Wire Wire Line
	2950 4100 2950 4650
Wire Wire Line
	4850 2200 4450 2200
Wire Wire Line
	4450 2200 4450 4500
Wire Wire Line
	4450 4500 3050 4500
Wire Wire Line
	2950 4650 4600 4650
Wire Wire Line
	4600 4650 4600 2350
Wire Wire Line
	4600 2350 5000 2350
Wire Wire Line
	5000 2350 5000 2200
$Comp
L R R?
U 1 1 59394766
P 5250 3950
F 0 "R?" V 5330 3950 50  0001 C CNN
F 1 "10k" V 5250 3950 50  0000 C CNN
F 2 "" V 5180 3950 50  0000 C CNN
F 3 "" H 5250 3950 50  0000 C CNN
	1    5250 3950
	0    1    1    0   
$EndComp
Wire Wire Line
	5400 3950 5450 3950
Connection ~ 5450 3950
Wire Wire Line
	5100 3950 5050 3950
Connection ~ 5050 3950
$Comp
L R R?
U 1 1 593948A4
P 4850 2500
F 0 "R?" V 4930 2500 50  0001 C CNN
F 1 "4.7k" V 4850 2500 50  0000 C CNN
F 2 "" V 4780 2500 50  0000 C CNN
F 3 "" H 4850 2500 50  0000 C CNN
	1    4850 2500
	0    1    1    0   
$EndComp
$Comp
L R R?
U 1 1 593948C0
P 4850 2700
F 0 "R?" V 4930 2700 50  0001 C CNN
F 1 "4.7k" V 4850 2700 50  0000 C CNN
F 2 "" V 4780 2700 50  0000 C CNN
F 3 "" H 4850 2700 50  0000 C CNN
	1    4850 2700
	0    1    1    0   
$EndComp
Wire Wire Line
	4450 2500 4700 2500
Connection ~ 4450 2500
Wire Wire Line
	4600 2700 4700 2700
Connection ~ 4600 2700
Wire Wire Line
	5000 2500 5600 2500
Connection ~ 5600 2500
Wire Wire Line
	5000 2700 5600 2700
Connection ~ 5600 2700
$EndSCHEMATC
