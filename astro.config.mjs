// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import fs from 'fs';

// https://astro.build/config
export default defineConfig({
  vite: {
    server: {
      allowedHosts: ['.hjkl01.cn'],
    }
  },
	integrations: [
		starlight({
			title: 'Github Repository',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/withastro/starlight' }],
			sidebar: fs.readdirSync('src/content/docs').filter(dir => {
          const stat = fs.statSync(`src/content/docs/${dir}`);
          return stat.isDirectory();
        }).map(dir => ({
          label: dir,
          autogenerate: { directory: dir },
          collapsed: true,
        })),
		}),
	],
});
