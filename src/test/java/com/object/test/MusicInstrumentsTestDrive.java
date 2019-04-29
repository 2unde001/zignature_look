package com.object.test;

import com.object.MusicInstruments;
import org.junit.Assert;
import org.junit.Test;

public class MusicInstrumentsTestDrive
{
    @Test
    public void validateInstrument()
    {
        MusicInstruments instruments = new MusicInstruments();

        Assert.assertEquals("Electric Guitars", instruments.setGuitar("Electric Guitars"));
        instruments.getGuiter();
        Assert.assertEquals(10,instruments.setNumberOfDrums(10));
        instruments.getNumberOfDrums();
        Assert.assertEquals(true,instruments.setRockStarUsesIt(true));
        instruments.getArockStarUsesIt();

    }
}
