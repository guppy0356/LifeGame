package com.gameoflife;

public class Grid {
    private boolean[][] cells;
    private final int rows;
    private final int cols;

    public Grid(int rows, int cols) {
        this.rows = rows;
        this.cols = cols;
        this.cells = new boolean[rows][cols];
    }

    public void setCellState(int row, int col, boolean isAlive) {
        cells[row][col] = isAlive;
    }

    public boolean getCellState(int row, int col) {
        return cells[row][col];
    }

    public int getRows() {
        return rows;
    }
    public int getCols() {
        return cols;
    }
