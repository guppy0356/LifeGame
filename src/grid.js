class Grid {
  constructor(width, height) {
    this.width = width;
    this.height = height;
    this.cells = Array(width * height).fill(null);
  }
}

module.exports = Grid;
