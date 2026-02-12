import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  async rewrites() {
    return [
      {
        source: '/mariaimg/:path*',
        destination: '/api/mariaimg/:path*',
      },
    ];
  },
  images: {
    remotePatterns: [
      {
        protocol: 'http',
        hostname: 'localhost',
        port: '3000',
        pathname: '/mariaimg/**',
      },
    ],
  },
};

export default nextConfig;
