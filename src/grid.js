export class Grid {
  constructor(rows, cols) {
    this.rows = rows;
    this.cols = cols;
    this.cells = Array(rows).fill().map(() => Array(cols).fill(null));
  }

  getCellValue(row, col) {
    if (row < 0 || row >= this.rows || col < 0 || col >= this.cols) {
      throw new Error('Cell coordinates out of bounds');
    }
    return this.cells[row][col];
  }

  get dimensions() {
    return [this.rows, this.cols];
  }
