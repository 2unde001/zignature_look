package com.object.test;

import com.object.Song;
import org.junit.Assert;
import org.junit.Test;

public class SongTestDrive
{
    @Test
    public void validateMusicPlayed(){
        Song song1 = new Song();

        Assert.assertEquals(true,song1.setArtist("Beyonce"));
        Assert.assertEquals(true,song1.setTitle("Lemonade"));

    }
}
