// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import fs from 'fs';

// https://astro.build/config
export default defineConfig({
  vite: {
    server: {
      allowedHosts: ['.hjkl01.cn'],
    },
    build: {
      rollupOptions: {
        output: {
          manualChunks: {
            vendor: ['astro'],
          },
        },
      },
    },
  },
  image: {
    domains: ['github.com', 'raw.githubusercontent.com'],
  },
  integrations: [
    starlight({
      title: 'Github Trending',
      description: 'A curated collection of useful GitHub repositories',
      social: [
        { icon: 'github', label: 'GitHub', href: 'https://github.com/withastro/starlight' }
      ],
      sidebar: fs.readdirSync('src/content/docs').filter(dir => {
        const stat = fs.statSync(`src/content/docs/${dir}`);
        return stat.isDirectory();
      }).map(dir => ({
        label: dir,
        autogenerate: { directory: dir },
        collapsed: true,
      })),

      editLink: {
        baseUrl: 'https://github.com/your-username/your-repo/edit/main/'
      },
    }),
  ],

});
