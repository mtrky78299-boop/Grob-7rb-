import subprocess
import sys
import os

print("🔧 جاري تجميع البرنامج...")

# الأوامر الموصى بها لـ Python 3.13
commands = [
    sys.executable, "-m", "PyInstaller",
    "--onefile",
    "--name", "محلل_كلمة_المرور",
    "--clean",
    "--noupx",  # إيقاف UPX مؤقتاً
    "--log-level=WARN",
    "محلل_كلمة_المرور.py"
]

try:
    subprocess.run(commands, check=True)
    print("✅ تم التجميع بنجاح!")
    print("📁 الملف في: dist/محلل_كلمة_المرور.exe")
except Exception as e:
    print(f"❌ خطأ: {e}")
    print("\n🔧 جرب الحلول البديلة...")
    
    # الحل البديل: استخدام Nuitka
    try:
        print("🔄 جرب استخدام Nuitka بدلاً من PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "nuitka"])
        subprocess.run([sys.executable, "-m", "nuitka", "--onefile", "محلل_كلمة_المرور.py"])
        print("✅ تم التجميع باستخدام Nuitka!")
    except:
        print("❌ فشل جميع المحاولات")