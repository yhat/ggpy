module.exports = function(grunt) {
	require('matchdep').filterDev('grunt-*').forEach(grunt.loadNpmTasks);

	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		banner: '/*\n<%= pkg.name %> - v<%= pkg.version %> - ' + '<%= grunt.template.today("yyyy-mm-dd") %>\n<%= pkg.description %>\nLovingly coded by <%= pkg.author.name %>  - <%= pkg.author.url %> \n*/\n',
		less: {
			dist: {
				options: {
					paths: ['css/less']
				},
				files: {
					'css/main.css': 'css/less/main.less'
				}
			}
		},
		cssmin: {
			combine: {
				options: {
					banner: '<%= banner %>'
				},
				files: {
					'css/<%= pkg.name %>.min.css': ['css/normalize.css', 'css/main.css']
				}
			}
		},
		concat: {
			options: {
				separator: '',
				stripBanners: {
					block: true,
					line: true
				},
				banner: '<%= banner %>'
			},
			dist: {
				src: ['js/lib/google-code-prettify/prettify.js'],
				dest: 'js/<%= pkg.name %>.js'
			}
		},
		uglify: {
			options: {
				banner: '<%= banner %>'
			},
			dist: {
				files: {
					'js/<%= pkg.name %>.min.js': ['<%= concat.dist.dest %>']
				}
			}
		},
		watch: {
			options: {
				livereload: true
			},
			less: {
				files: ['css/less/*.less'],
				tasks: ['less:dist']
			},
			cssmin: {
				files: ['css/*.css'],
				tasks: ['cssmin']
			},
			concat: {
				files: ['js/main.js', 'js/lib/*.js'],
				tasks: ['concat:dist']
			},
			uglify: {
				files: ['js/<%= pkg.name %>.js'],
				tasks: ['uglify:dist']
			},
			php: {
				files: '**/*.php',
			}
		}
	});
	
	grunt.registerTask('build', [
		'less:dist',
		'cssmin',
		'concat:dist',
		'uglify:dist'
	]);
	
	grunt.registerTask('server', [
		'less:dist',
		'cssmin',
		'concat:dist',
		'uglify:dist',
		'watch'
	]);

	grunt.registerTask('default', 'build');
}
