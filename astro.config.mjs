// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

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
			sidebar: [
				{
					label: 'Guides',
					items: [
						// Each item here is one entry in the navigation menu.
						{ label: 'Example Guide', slug: 'guides/example' },
					],
				},
				{
					label: 'Github',
					autogenerate: { directory: 'github' },
				},
				// {
				// 	label: 'Hello Github',
				// 	autogenerate: { directory: 'hellogithub' },
				// },
			],
		}),
	],
});
