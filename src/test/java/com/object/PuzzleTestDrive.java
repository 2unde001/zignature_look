package com.object;

import org.junit.Test;

public class PuzzleTestDrive
{
    Puzzle[] puzzle = new Puzzle[6];
    private int y = 1;
    private int x;
    private int result;


    @Test
    public void validatePuzzleSolution()
    {
        while (x < 6)
        {
            puzzle[x] = new Puzzle();
            puzzle[x].ivar = y;
            y = y * 10;
            x = x + 1;

        }
        x = 6;

        while (x > 0){
            x = x - 1;
            result = result + puzzle[x].doStuff(x);
        }
        System.out.println("result " + result);
    }
}
