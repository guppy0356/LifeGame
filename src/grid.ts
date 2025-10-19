type Cell = 0 | 1;

export class Grid {
  private cells: Cell[][];
  private width: number;
  private height: number;

  constructor(width: number, height: number) {
    this.width = width;
    this.height = height;
    this.cells = Array(height)
      .fill(0)
      .map(() => Array(width).fill(0));
  }

  public getCell(x: number, y: number): Cell {
    if (this.isWithinBounds(x, y)) {
      return this.cells[y][x];
    }
    return 0;
  }

  public setCell(x: number, y: number, state: Cell): void {
    if (this.isWithinBounds(x, y)) {
      this.cells[y][x] = state;
    }
  }

  public toggleCell(x: number, y: number): void {
    if (this.isWithinBounds(x, y)) {
      this.cells[y][x] = this.cells[y][x] === 0 ? 1 : 0;
    }
  }

  private isWithinBounds(x: number, y: number): boolean {
    return x >= 0 && x < this.width && y >= 0 && y < this.height;
  }

  public getSize(): { width: number; height: number } {
    return {
      width: this.width,
      height: this.height
    };
