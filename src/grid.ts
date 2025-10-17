export class Grid {
    private width: number;
    private height: number;
    private cells: boolean[][];

    constructor(width: number, height: number) {
        this.width = width;
        this.height = height;
        this.cells = Array(height).fill(null)
            .map(() => Array(width).fill(false));
    }

    getWidth(): number {
        return this.width;
    }

    getHeight(): number {
        return this.height;
    }

    getCell(x: number, y: number): boolean {
        if (x < 0 || x >= this.width || y < 0 || y >= this.height) {
            return false;
        }
        return this.cells[y][x];
    }

    setCell(x: number, y: number, value: boolean): void {
        this.cells[y][x] = value;
    }
