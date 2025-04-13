import time
import random

# Simulated actuator function
def activate_emergency_brake():
    print("🚨 Emergency Brake Activated! Bike is stopping...")

# Simulated sensor reading functions
def read_blood_pressure():
    systolic = random.randint(85, 160)
    diastolic = random.randint(55, 100)
    return systolic, diastolic

def read_pulse_rate():
    return random.randint(50, 130)

def read_spo2():
    return random.randint(90, 100)

def detect_vibration():
    return random.choice([0, 1])

def read_helmet_status():
    return random.choice([0, 1])

# Check critical sensor abnormalities
def is_critical(bp_sys, bp_dia, pulse, spo2):
    bp_abnormal = bp_sys < 90 or bp_sys > 140 or bp_dia < 60 or bp_dia > 90
    pulse_abnormal = pulse < 60 or pulse > 110
    spo2_abnormal = spo2 < 94
    return bp_abnormal, pulse_abnormal, spo2_abnormal

# Decision making
def evaluate_system(bp_sys, bp_dia, pulse, spo2, vibration, helmet_worn):
    # Analyze each sensor
    bp_flag, pulse_flag, spo2_flag = is_critical(bp_sys, bp_dia, pulse, spo2)
    critical_flags = [bp_flag, pulse_flag, spo2_flag]
    support_flags = [not helmet_worn, vibration == 1]

    # Count number of abnormal readings
    total_critical = sum(critical_flags)
    total_support = sum(support_flags)

    # Logic: Alert only if 2+ flags (at least 1 critical)
    if total_critical >= 1 and (total_critical + total_support) >= 2:
        return True
    return False

# Main System
def main():
    print("🪖 Smart Bio Helmet System – Advanced Safety Mode")
    while True:
        # Read sensor values
        bp_sys, bp_dia = read_blood_pressure()
        pulse = read_pulse_rate()
        spo2 = read_spo2()
        vibration = detect_vibration()
        helmet_worn = read_helmet_status()

        # Display Readings
        print("\n--- SENSOR DATA ---")
        print(f"🩺 Blood Pressure: {bp_sys}/{bp_dia} mmHg")
        print(f"❤️ Pulse Rate: {pulse} bpm")
        print(f"🩸 SpO2: {spo2}%")
        print(f"🪖 Helmet Worn: {'Yes' if helmet_worn else 'No'}")
        print(f"💥 Vibration Detected: {'Yes' if vibration else 'No'}")

        # Evaluate system status
        emergency = evaluate_system(bp_sys, bp_dia, pulse, spo2, vibration, helmet_worn)

        if emergency:
            print("\n🚨 CRITICAL CONDITION DETECTED!")
            activate_emergency_brake()
        else:
            print("\n✅ All Parameters Within Safe Limits.")

        print("--------------------------------------")
        time.sleep(5)

if __name__ == "__main__":
    main()




# activate_emergency_brake() would control GPIO pins on a Arduino to activate an electronic actuator (like a motor driver or solenoid to pull the brake).

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
BRAKE_PIN = 18
GPIO.setup(BRAKE_PIN, GPIO.OUT)

def activate_emergency_brake():
    GPIO.output(BRAKE_PIN, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(BRAKE_PIN, GPIO.LOW)

