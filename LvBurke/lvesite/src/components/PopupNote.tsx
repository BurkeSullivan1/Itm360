'use client';

import { motion, AnimatePresence } from 'framer-motion';

interface PopupNoteProps {
  isOpen: boolean;
  onClose: () => void;
}

export default function PopupNote({ isOpen, onClose }: PopupNoteProps) {
  return (
    <AnimatePresence>
      {isOpen && (
        <motion.div
          className="fixed inset-0 bg-navy/90 backdrop-blur-sm z-50 flex items-center justify-center p-8"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.3 }}
          onClick={onClose}
        >
          <motion.div
            className="bg-navy/95 border border-gold/30 rounded-3xl p-8 max-w-2xl w-full relative shadow-2xl"
            initial={{ opacity: 0, scale: 0.8, y: 50 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.8, y: 50 }}
            transition={{ duration: 0.4, ease: "easeOut" }}
            onClick={(e) => e.stopPropagation()}
          >
            {/* Close button */}
            <motion.button
              onClick={onClose}
              className="absolute top-4 right-4 p-2 text-cream/60 hover:text-cream transition-colors rounded-full hover:bg-gold/10"
              whileHover={{ scale: 1.1 }}
              whileTap={{ scale: 0.9 }}
            >
              <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clipRule="evenodd" />
              </svg>
            </motion.button>

            {/* Header */}
            <motion.div
              className="text-center mb-8"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.2 }}
            >
              <h2 className="text-3xl font-light text-gold mb-2">My Heart to Yours</h2>
              <div className="w-24 h-px bg-gradient-to-r from-transparent via-gold to-transparent mx-auto"></div>
            </motion.div>

            {/* Note content */}
            <motion.div
              className="space-y-6 text-cream leading-relaxed"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.4 }}
            >
              <p className="text-lg font-light">
                Maria,
              </p>
              
              <p>
                I created this for you because words sometimes aren't enough, but memories... 
                memories are everything. Each photo here holds a piece of us, a moment where 
                time stopped and everything felt perfect.
              </p>
              
              <p>
                I know things are complicated right now, and I know it's hard for us to talk. 
                But I needed you to see this - to remember what we had, what we built together, 
                and how beautiful our story was.
              </p>
              
              <p>
                Every smile, every laugh, every quiet moment we shared - they're all here, 
                waiting for you. These aren't just photos; they're proof that what we had 
                was real, was special, was worth everything.
              </p>
              
              <p>
                I hope when you see these, you remember not just the moments, but how they felt. 
                How we felt. How right everything was when we were together.
              </p>
              
              <p className="text-gold font-light italic pt-4">
                With all my love, always
              </p>
            </motion.div>

            {/* Heart decoration */}
            <motion.div
              className="flex justify-center mt-8"
              initial={{ opacity: 0, scale: 0 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ delay: 0.8, type: "spring" }}
            >
              <svg className="w-8 h-8 text-gold/60" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clipRule="evenodd" />
              </svg>
            </motion.div>
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
