const fs = require('fs');
const path = require('path');

const root = __dirname;
const commonFiles = ['gesture-handler.js', 'gesture-detector.js', 'styles.css'];

function isTargetFolder(name) {
  return /^\d+$/.test(name);
}

function updateHtmlFile(filePath) {
  if (!fs.existsSync(filePath)) return;
  let content = fs.readFileSync(filePath, 'utf8');
  let changed = false;
  // Заменить подключения стилей
  content = content.replace(/<link rel="stylesheet" href="styles.css"\s*\/?>(\s*)/g, '<link rel="stylesheet" href="../common/styles.css">$1');
  // Заменить подключения gesture-detector.js и gesture-handler.js
  content = content.replace(/<script src="gesture-detector.js"><\/script>\s*/g, '<script src="../common/gesture-detector.js"></script>\n');
  content = content.replace(/<script src="gesture-handler.js"><\/script>\s*/g, '<script src="../common/gesture-handler.js"></script>\n');
  // Для self-closing <link ... />
  content = content.replace(/<link rel="stylesheet" href="styles.css"\s*\/>/g, '<link rel="stylesheet" href="../common/styles.css" />');
  // Для self-closing <script ... />
  content = content.replace(/<script src="gesture-detector.js"\s*\/>/g, '<script src="../common/gesture-detector.js" />');
  content = content.replace(/<script src="gesture-handler.js"\s*\/>/g, '<script src="../common/gesture-handler.js" />');
  fs.writeFileSync(filePath, content, 'utf8');
}

function cleanupFolder(folderPath) {
  // Удалить дублирующие js/css
  for (const file of commonFiles) {
    const fileToDelete = path.join(folderPath, file);
    if (fs.existsSync(fileToDelete)) {
      fs.unlinkSync(fileToDelete);
    }
  }
  // Обновить index.html и image-tracking.html
  updateHtmlFile(path.join(folderPath, 'index.html'));
  updateHtmlFile(path.join(folderPath, 'image-tracking.html'));
}

fs.readdirSync(root, { withFileTypes: true })
  .filter(dirent => dirent.isDirectory() && isTargetFolder(dirent.name))
  .forEach(dirent => {
    const folderPath = path.join(root, dirent.name);
    cleanupFolder(folderPath);
    console.log('Обработана папка:', dirent.name);
  });

console.log('Готово! Все папки обработаны.');
