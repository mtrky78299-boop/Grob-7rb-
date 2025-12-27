# حفظ هذا الكود كـ create_icon.py
from PIL import Image, ImageDraw
import os

# إنشاء أيقونة بسيطة
img = Image.new('RGB', (256, 256), color='#1a1a2e')
draw = ImageDraw.Draw(img)
draw.ellipse([50, 50, 206, 206], fill='#16213e', outline='#0f3460')
draw.ellipse([70, 70, 186, 186], fill='#0f3460')
draw.text((100, 120), "🔐", fill='#e94560', font=None)

# حفظ كـ ICO
img.save('icon.ico', format='ICO')
print("✅ تم إنشاء الأيقونة")