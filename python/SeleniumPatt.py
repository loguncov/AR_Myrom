import os
import time
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

qr_dir = "qr_codes"  # Папка с сгенерированными QR кодами (png)
out_dir = "patt"  # Папка для сохранения .patt
os.makedirs(out_dir, exist_ok=True)

chrome_options = Options()
prefs = {
    "download.default_directory": os.path.abspath(out_dir),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
}
chrome_options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 20)

def process(file_path, num):
    print(f"Загружаю: {file_path}")
    file_input = wait.until(EC.presence_of_element_located((By.ID, "fileinput")))
    file_input.send_keys(file_path)
    print("Файл загружен")

    # Клик по "Download Marker"
    dl_marker_btn = wait.until(EC.element_to_be_clickable((By.ID, "buttonDownloadEncoded")))
    dl_marker_btn.click()
    print("Скачиваю .patt")
    time.sleep(2)

    # Переименовать .patt
    patt_file = os.path.join(out_dir, "pattern-marker.patt")
    new_patt = os.path.join(out_dir, f"{num:02d}.patt")
    if os.path.exists(patt_file):
        shutil.move(patt_file, new_patt)
        print(f"Сохраняю {new_patt}")

    # Клик по "Download Image"
    dl_img_btn = wait.until(EC.element_to_be_clickable((By.ID, "buttonDownloadFullImage")))
    driver.execute_script("arguments[0].scrollIntoView(true);", dl_img_btn)
    time.sleep(0.2)
    driver.execute_script("""
        var tips = document.querySelectorAll('.mdl-tooltip.is-active');
        tips.forEach(function(tip){ tip.style.display='none'; });
    """)
    time.sleep(0.2)
    driver.execute_script("arguments[0].click();", dl_img_btn)
    print("Скачиваю .png")
    time.sleep(2)

    # Переименовать скачанную картинку (.png/.jpg)
    for fname in os.listdir(out_dir):
        if fname.startswith("pattern-marker.") and not fname.endswith(".patt"):
            ext = os.path.splitext(fname)[1]
            src_img = os.path.join(out_dir, fname)
            new_img = os.path.join(out_dir, f"{num:02d}{ext}")
            shutil.move(src_img, new_img)
            print(f"Сохраняю {new_img}")

    driver.refresh()
    time.sleep(2)

driver.get("https://jeromeetienne.github.io/AR.js/three.js/examples/marker-training/examples/generator.html")
files = sorted([f for f in os.listdir(qr_dir) if f.lower().endswith('.png') or f.lower().endswith('.jpg')])
for idx, fname in enumerate(files, 1):
    full_path = os.path.abspath(os.path.join(qr_dir, fname))
    process(full_path, idx)

driver.quit()
