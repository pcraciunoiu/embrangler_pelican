'use strict';

module.exports = function (grunt) {
  require('jit-grunt')(grunt);

  grunt.initConfig({

    embrangler: {
      theme: 'themes/embrangler',
    },
    watch: {
      sass: {
        files: [
          '<%= embrangler.theme %>/static/sass/**/*.{scss,sass}'],
        tasks: ['sass', 'autoprefixer']
      },
      gruntfile: {
        files: ['Gruntfile.js']
      },
      livereload: {
        files: [
          '<%= embrangler.theme %>/**/*.css',
          '<%= embrangler.theme %>/**/*.html',
          '<%= embrangler.theme %>/**/*.js'
        ],
        options: {
          livereload: true
        }
      },
    },

    autoprefixer: {
      options: {
        browsers: ['last 1 version']
      },
      dist: {
        files: [{
          expand: true,
          cwd: '<%= embrangler.theme %>/static/css',
          src: '*.css',
          dest: '<%= embrangler.theme %>/static/css'
        }]
      }
    },

    sass: {
      server: {
        options: {
          loadPath: [
            '<%= embrangler.theme %>/static/sass',
            '<%= embrangler.theme %>/static/bower_components',
          ]
        },
        files: {
          '<%= embrangler.theme %>/static/css/main.css' : '<%= embrangler.theme %>/static/sass/main.scss'
        }
      }
    }
  });

  grunt.registerTask('default', [
    'sass',
    'autoprefixer',
    'watch'
  ]);
};
