#!/usr/bin/node
/* Define class Rectangle */
class Rectangle {
  /* constructor receive 2 arguments
and validate if argument is greather
than zero */
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    /* instance method that print the rectangle */
    let a = this.height;
    while (a > 0) {
      console.log('X'.repeat(this.width));
      a--;
    }
  }

  double () {
    /* instnace method that duplicate the size */
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }
}
module.exports = Rectangle;
