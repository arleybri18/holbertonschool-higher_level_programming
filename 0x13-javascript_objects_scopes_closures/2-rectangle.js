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
}
module.exports = Rectangle;
