package com.object;

public class DrumKit
{
    public boolean snare;

    public String playSnare()
    {
        System.out.print("bang bang -ba-bang");
        return String.format("bang bang ba-bang").trim();
    }
}
