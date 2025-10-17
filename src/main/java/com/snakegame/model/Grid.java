package com.snakegame.model;

import java.util.Arrays;

public class Grid {
    private int[][] grid;
    private final int width;
    private final int height;

    public Grid(int width, int height) {
        this.width = width;
        this.height = height;
        this.grid = new int[height][width];
        initializeGrid();
    }

    private void initializeGrid() {
        for (int[] row : grid) {
            Arrays.fill(row, 0);
        }
    }

    public void setValue(int x, int y, int value) {
        validateCoordinates(x, y);
        grid[y][x] = value;
    }

    public int getValue(int x, int y) {
        validateCoordinates(x, y);
        return grid[y][x];
    }

    private void validateCoordinates(int x, int y) {
        if (x < 0 || x >= width || y < 0 || y >= height) {
            throw new IllegalArgumentException("Coordinates out of bounds");
        }
    }

    public void clear() {
        initializeGrid();
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int[] row : grid) {
            sb.append(Arrays.toString(row)).append("\n");
        }
        return sb.toString();
    }
