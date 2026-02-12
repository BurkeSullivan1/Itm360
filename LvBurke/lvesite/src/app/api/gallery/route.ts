import { NextResponse } from 'next/server';
import { promises as fs } from 'fs';
import path from 'path';
import { MediaItem } from '@/lib/gallery';

async function loadJsonFile<T>(filePath: string, fallback: T): Promise<T> {
  try {
    const fullPath = path.join(process.cwd(), filePath);
    const content = await fs.readFile(fullPath, 'utf-8');
    return JSON.parse(content);
  } catch (error) {
    console.warn(`Could not load ${filePath}, using fallback:`, error);
    return fallback;
  }
}

export async function GET() {
  try {
    const [galleryData, captionsData, subtitlesData] = await Promise.all([
      loadJsonFile<MediaItem[]>('content/gallery.json', []),
      loadJsonFile<Record<string, string>>('content/captions.json', {}),
      loadJsonFile<string[]>('content/subtitles.json', [
        'I still smile at this one',
        'Our song on the radio',
        'You make ordinary moments magical',
        'Every day with you is a new adventure',
        'Your hand in mine feels like home',
        'The way you laugh at my terrible jokes',
        'Dancing in the kitchen at midnight',
        'You\'re my favorite notification',
        'Coffee tastes better with you',
        'These moments are everything'
      ])
    ]);

    // Merge gallery data with captions
    const items: MediaItem[] = galleryData.map((item: MediaItem) => {
      const filename = item.src.split('/').pop() || '';
      const caption = captionsData[filename];
      
      return {
        ...item,
        caption,
      };
    });

    const response = {
      items,
      subtitles: subtitlesData,
    };

    return NextResponse.json(response);
  } catch (error) {
    console.error('Error loading gallery data:', error);
    
    // Return fallback data
    return NextResponse.json({
      items: [],
      subtitles: [
        'I still smile at this one',
        'Our song on the radio',
        'You make ordinary moments magical'
      ]
    });
  }
}
