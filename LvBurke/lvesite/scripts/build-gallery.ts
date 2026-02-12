import fs from 'fs';
import path from 'path';
import sharp from 'sharp';

interface MediaFile {
  src: string;
  width?: number;
  height?: number;
  type: 'image' | 'video';
  duration?: number;
  dateCreated?: string;
}

const MARIA_IMG_DIR = path.join(process.cwd(), '..', 'mariaimg');
const OUTPUT_FILE = path.join(process.cwd(), 'content', 'gallery.json');

// Supported file types
const IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.avif'];
const VIDEO_EXTENSIONS = ['.mp4', '.mov', '.webm', '.avi'];

async function getImageDimensions(filePath: string): Promise<{ width: number; height: number }> {
  try {
    const metadata = await sharp(filePath).metadata();
    return {
      width: metadata.width || 0,
      height: metadata.height || 0,
    };
  } catch (error) {
    console.warn(`Failed to get dimensions for ${filePath}:`, error);
    return { width: 0, height: 0 };
  }
}

async function getVideoDuration(filePath: string): Promise<number | undefined> {
  // For now, we'll return undefined. In a full implementation,
  // you could use ffprobe-static to get video duration
  try {
    // This is a placeholder - you can implement ffprobe integration here
    return undefined;
  } catch (error) {
    console.warn(`Failed to get duration for ${filePath}:`, error);
    return undefined;
  }
}

function getFileStats(filePath: string): string | undefined {
  try {
    const stats = fs.statSync(filePath);
    return stats.mtime.toISOString();
  } catch (error) {
    console.warn(`Failed to get file stats for ${filePath}:`, error);
    return undefined;
  }
}

function isImageFile(filename: string): boolean {
  const ext = path.extname(filename).toLowerCase();
  return IMAGE_EXTENSIONS.includes(ext);
}

function isVideoFile(filename: string): boolean {
  const ext = path.extname(filename).toLowerCase();
  return VIDEO_EXTENSIONS.includes(ext);
}

function naturalSort(a: string, b: string): number {
  return a.localeCompare(b, undefined, { numeric: true, sensitivity: 'base' });
}

async function buildGallery() {
  console.log('🖼️ Building gallery from mariaimg folder...');

  // Check if mariaimg directory exists
  if (!fs.existsSync(MARIA_IMG_DIR)) {
    console.log('📁 Creating mariaimg directory for you to add photos and videos...');
    fs.mkdirSync(MARIA_IMG_DIR, { recursive: true });
    
    // Create a sample file to demonstrate
    const sampleContent = 'Add your photos and videos to this folder, then run npm run build:gallery';
    fs.writeFileSync(path.join(MARIA_IMG_DIR, 'README.txt'), sampleContent);
  }

  // Get all files from mariaimg directory
  const files = fs.readdirSync(MARIA_IMG_DIR);
  const mediaFiles: MediaFile[] = [];

  // Filter and process media files
  const validFiles = files.filter(file => 
    isImageFile(file) || isVideoFile(file)
  ).sort(naturalSort);

  console.log(`📸 Found ${validFiles.length} media files to process...`);

  for (const file of validFiles) {
    const fullPath = path.join(MARIA_IMG_DIR, file);
    const relativePath = `/mariaimg/${file}`;
    
    console.log(`Processing: ${file}`);

    const mediaFile: MediaFile = {
      src: relativePath,
      type: isImageFile(file) ? 'image' : 'video',
      dateCreated: getFileStats(fullPath),
    };

    if (isImageFile(file)) {
      const dimensions = await getImageDimensions(fullPath);
      mediaFile.width = dimensions.width;
      mediaFile.height = dimensions.height;
    } else if (isVideoFile(file)) {
      mediaFile.duration = await getVideoDuration(fullPath);
    }

    mediaFiles.push(mediaFile);
  }

  // Sort by date created if available, otherwise by filename
  mediaFiles.sort((a, b) => {
    if (a.dateCreated && b.dateCreated) {
      return new Date(a.dateCreated).getTime() - new Date(b.dateCreated).getTime();
    }
    return naturalSort(a.src, b.src);
  });

  // Ensure content directory exists
  const contentDir = path.dirname(OUTPUT_FILE);
  if (!fs.existsSync(contentDir)) {
    fs.mkdirSync(contentDir, { recursive: true });
  }

  // Write gallery.json
  fs.writeFileSync(OUTPUT_FILE, JSON.stringify(mediaFiles, null, 2));

  console.log(`✅ Gallery built successfully! ${mediaFiles.length} files processed.`);
  console.log(`📄 Output: ${OUTPUT_FILE}`);
}

// Run the script
buildGallery().catch(console.error);
