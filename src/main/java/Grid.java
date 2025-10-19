public class Grid {
    private final int width;
    private final int height;
    private final boolean[][] cells;

    public Grid(int width, int height) {
        if (width <= 0 || height <= 0) {
            throw new IllegalArgumentException("Grid dimensions must be positive");
        }

        this.width = width;
        this.height = height;
        this.cells = new boolean[height][width];
    }

    public boolean getCell(int x, int y) {
        validateCoordinates(x, y);
        return cells[y][x];
    }

    public void setCell(int x, int y, boolean value) {
        validateCoordinates(x, y);
        cells[y][x] = value;
    }

    private void validateCoordinates(int x, int y) {
        if (x < 0 || x >= width || y < 0 || y >= height) {
            throw new IllegalArgumentException("Coordinates out of bounds");
        }
    }

    public int getWidth() { return width; }

    public int getHeight() { return height; }
}
