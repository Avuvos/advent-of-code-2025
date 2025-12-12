from dataclasses import dataclass
from pathlib import Path


class Shape:
    """A set of cells that can be rotated, flipped, and normalized."""
    
    def __init__(self, cells: set[tuple[int, int]]):
        self.cells = cells
    
    @classmethod
    def from_grid(cls, grid: list[list[str]]) -> "Shape":
        cells = {
            (x, y) for y, row in enumerate(grid) for x, ch in enumerate(row) if ch == "#"
        }
        return cls(cells)
    
    def normalize(self) -> tuple[tuple[int, int], ...]:
        """Translate to origin and return as sorted tuple (hashable)."""
        min_x = min(x for x, _ in self.cells)
        min_y = min(y for _, y in self.cells)
        return tuple(sorted((x - min_x, y - min_y) for x, y in self.cells))
    
    def rotate(self) -> "Shape":
        """Rotate 90 degrees clockwise."""
        return Shape({(y, -x) for x, y in self.cells})
    
    def flip(self) -> "Shape":
        """Flip horizontally."""
        return Shape({(-x, y) for x, y in self.cells})
    
    def all_orientations(self) -> list["Shape"]:
        """Get all unique orientations (rotations + flips)."""
        seen: set[tuple[tuple[int, int], ...]] = set()
        cur = self
        for _ in range(4):
            seen.add(cur.normalize())
            seen.add(cur.flip().normalize())
            cur = cur.rotate()
        return [Shape(set(s)) for s in seen]


class Present:
    """A present shape that can be rotated and flipped."""
    
    def __init__(self, index: int, shape: Shape):
        self.index = index
        self.shape = shape
        self.area = len(shape.cells)
        self.orientations = shape.all_orientations()
    
    @classmethod
    def from_grid(cls, index: int, grid: list[list[str]]) -> "Present":
        return cls(index, Shape.from_grid(grid))
    
    def placement_masks(self, w: int, h: int) -> list[int]:
        """Generate all valid placement bitmasks for this present in a grid."""
        masks: list[int] = []
        for shape in self.orientations:
            max_x = max(x for x, _ in shape.cells)
            max_y = max(y for _, y in shape.cells)
            for dy in range(h - max_y):
                for dx in range(w - max_x):
                    mask = 0
                    for x, y in shape.cells:
                        mask |= 1 << ((y + dy) * w + (x + dx))
                    masks.append(mask)
        return masks


@dataclass
class Region:
    """A region under a tree where presents need to fit."""
    
    w: int
    h: int
    counts: list[int]


def can_fit(region: Region, presents: list[Present]) -> bool:
    """Check if all required presents can fit in the region."""
    total_area = sum(c * presents[i].area for i, c in enumerate(region.counts))
    if total_area > region.w * region.h:
        return False
    
    pieces: list[list[int]] = []
    for i, count in enumerate(region.counts):
        masks = presents[i].placement_masks(region.w, region.h)
        pieces.extend([masks] * count)
    pieces.sort(key=len)
    
    def backtrack(idx: int, occupied: int) -> bool:
        if idx == len(pieces):
            return True
        for mask in pieces[idx]:
            if occupied & mask:
                continue
            if backtrack(idx + 1, occupied | mask):
                return True
        return False
    
    return backtrack(0, 0)


def parse_input(data: str) -> tuple[list[Present], list[Region]]:
    """Parse input into presents and regions."""
    presents: dict[int, Present] = {}
    regions: list[Region] = []
    
    for block in data.split("\n\n"):
        block = block.strip()
        if not block:
            continue
        
        lines = [ln.strip() for ln in block.splitlines() if ln.strip()]
        header = lines[0]
        
        if header.endswith(":") and header[:-1].isdigit():
            idx = int(header[:-1])
            grid = [list(row) for row in lines[1:]]
            presents[idx] = Present.from_grid(idx, grid)
        else:
            for line in lines:
                dims, nums = line.split(":", 1)
                w, h = map(int, dims.strip().split("x"))
                counts = [int(x) for x in nums.split()]
                regions.append(Region(w, h, counts))
    
    present_list = [presents[i] for i in range(max(presents) + 1)]
    return present_list, regions


def solve(data: str) -> int:
    presents, regions = parse_input(data)
    return sum(1 for region in regions if can_fit(region, presents))


if __name__ == "__main__":
    input_data = (Path(__file__).parent / "input.txt").read_text().strip()
    print(solve(input_data))
