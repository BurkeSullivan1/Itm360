'use client';

import { motion } from 'framer-motion';

interface ControlsProps {
  isPlaying: boolean;
  currentIndex: number;
  totalItems: number;
  onPlayPause: () => void;
  onPrevious: () => void;
  onNext: () => void;
  onShare?: () => void;
}

export default function Controls({
  isPlaying,
  currentIndex,
  totalItems,
  onPlayPause,
  onPrevious,
  onNext,
  onShare,
}: ControlsProps) {
  return (
    <motion.div
      className="fixed bottom-[calc(env(safe-area-inset-bottom)+1rem)] md:bottom-8 left-1/2 transform -translate-x-1/2 bg-navy/80 backdrop-blur-sm border border-gold/20 rounded-2xl px-4 py-3 md:px-6 md:py-4"
      initial={{ opacity: 0, y: 50 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <div className="flex items-center space-x-4 md:space-x-6">
        {/* Previous button */}
        <motion.button
          onClick={onPrevious}
          className="p-2 text-cream hover:text-gold transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-gold/50 rounded-lg"
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.9 }}
          aria-label="Previous"
        >
          <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
            <path fillRule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clipRule="evenodd" />
          </svg>
        </motion.button>

        {/* Play/Pause button */}
        <motion.button
          onClick={onPlayPause}
          className="p-3 bg-gold/20 hover:bg-gold/30 text-cream rounded-full transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-gold/50"
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.9 }}
          aria-label={isPlaying ? 'Pause' : 'Play'}
        >
          {isPlaying ? (
            <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zM7 8a1 1 0 012 0v4a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v4a1 1 0 102 0V8a1 1 0 00-1-1z" clipRule="evenodd" />
            </svg>
          ) : (
            <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clipRule="evenodd" />
            </svg>
          )}
        </motion.button>

        {/* Next button */}
        <motion.button
          onClick={onNext}
          className="p-2 text-cream hover:text-gold transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-gold/50 rounded-lg"
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.9 }}
          aria-label="Next"
        >
          <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
            <path fillRule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clipRule="evenodd" />
          </svg>
        </motion.button>

        {/* Counter */}
        <div className="text-cream/80 text-xs md:text-sm font-medium px-2 md:px-4">
          {currentIndex + 1} of {totalItems}
        </div>

        {/* Share button */}
        {onShare && (
          <motion.button
            onClick={onShare}
            className="p-2 text-cream hover:text-gold transition-colors duration-200 focus:outline-none focus:ring-2 focus:ring-gold/50 rounded-lg"
            whileHover={{ scale: 1.1 }}
            whileTap={{ scale: 0.9 }}
            aria-label="Share"
          >
            <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
              <path d="M15 8a3 3 0 10-2.977-2.63l-4.94 2.47a3 3 0 100 4.319l4.94 2.47a3 3 0 10.895-1.789l-4.94-2.47a3.027 3.027 0 000-.74l4.94-2.47C13.456 7.68 14.19 8 15 8z" />
            </svg>
          </motion.button>
        )}
      </div>

      {/* Progress bar */}
      <motion.div 
        className="mt-4 h-1 bg-navy/60 rounded-full overflow-hidden"
        initial={{ scaleX: 0 }}
        animate={{ scaleX: 1 }}
        transition={{ duration: 0.5, delay: 0.2 }}
      >
        <motion.div
          className="h-full bg-gradient-to-r from-gold/60 to-gold rounded-full"
          initial={{ width: '0%' }}
          animate={{ width: `${((currentIndex + 1) / totalItems) * 100}%` }}
          transition={{ duration: 0.3 }}
        />
      </motion.div>
    </motion.div>
  );
}
