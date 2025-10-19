#pragma once

#include <vector>
#include <cstddef>

class Grid {
public:
    Grid(size_t width, size_t height)
        : width_(width)
        , height_(height)
        , cells_(width * height, false)
    {}

    bool getCellState(size_t x, size_t y) const {
        return cells_[y * width_ + x];
    }

    void setCellState(size_t x, size_t y, bool alive) {
        cells_[y * width_ + x] = alive;
    }

    size_t getWidth() const {
        return width_;
    }

    size_t getHeight() const {
        return height_;
    }

private:
    size_t width_;
    size_t height_;
    std::vector<bool> cells_;
};
