var gulp = require('gulp');
var browserSync = require('browser-sync').create();

var sass = require('gulp-sass');

var runSequence = require('run-sequence');

gulp.task('watch', ['browserSync', 'sass'], function (){
  gulp.watch('app/styles/**/*.scss', ['sass']); 
  gulp.watch('**/*.html', browserSync.reload); 
  gulp.watch('app/js/**/*.js', browserSync.reload); 
});

gulp.task('browserSync', function() {
  browserSync.init({
    server: {
      baseDir: ''
    }
  })
})

gulp.task('sass', function(){
  return gulp.src('app/styles/main.scss')
    .pipe(sass()) 
    .pipe(gulp.dest('app/styles'))
    .pipe(browserSync.reload({
      stream: true
    }))
});

