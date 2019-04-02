package com.object;

public class Song
{
    private String title;
    private String artist;

    public boolean setArtist(String value)
    {
        artist = value;
        System.out.println("Artist name is " + artist);
        return artist.equals("Beyonce");
    }

    public boolean setTitle(String value)
    {
        title = value;
        System.out.println("Song title is " + title);
        return title.equals("Lemonade");
    }
}
