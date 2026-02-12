export interface MediaItem {
  src: string;
  width?: number;
  height?: number;
  type: 'image' | 'video';
  duration?: number;
  dateCreated?: string;
  caption?: string;
}

export interface GalleryData {
  items: MediaItem[];
  subtitles: string[];
}

let galleryCache: GalleryData | null = null;

export async function getGalleryData(): Promise<GalleryData> {
  if (galleryCache) {
    return galleryCache;
  }

  try {
    // Fetch gallery data from API route
    const response = await fetch('/api/gallery');
    if (!response.ok) {
      throw new Error('Failed to fetch gallery data');
    }
    
    const data = await response.json();
    galleryCache = data;
    return data;
  } catch (error) {
    console.warn('Could not load gallery data:', error);
    // Return fallback data
    return {
      items: [],
      subtitles: [
        'I still smile at this one',
        'Our song on the radio',
        'You make ordinary moments magical'
      ]
    };
  }
}

export async function getMediaItem(index: number): Promise<MediaItem | null> {
  const data = await getGalleryData();
  return data.items[index] || null;
}

export async function getTotalItems(): Promise<number> {
  const data = await getGalleryData();
  return data.items.length;
}

export async function getRandomSubtitle(): Promise<string> {
  const data = await getGalleryData();
  const randomIndex = Math.floor(Math.random() * data.subtitles.length);
  return data.subtitles[randomIndex];
}

export async function getPreviousIndex(currentIndex: number): Promise<number> {
  const total = await getTotalItems();
  return currentIndex === 0 ? total - 1 : currentIndex - 1;
}

export async function getNextIndex(currentIndex: number): Promise<number> {
  const total = await getTotalItems();
  return currentIndex === total - 1 ? 0 : currentIndex + 1;
}
