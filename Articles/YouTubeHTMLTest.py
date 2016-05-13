import unittest
import YouTubeHTML as y

url = "https://www.youtube.com/watch?v=gmvwZRwn-j0/0.jpg"
html = y.YouTubeHTML(url)

class TestYoutubeHTML(unittest.TestCase):

    def testIsTitleCorrect(self):
        self.assertEqual(html.title, "Piano chords for beginners: learn four chords to play hundreds of songs")

    def testIsTitleCorrect(self):
        self.assertEqual(html.username, "Bill Hilton")

if __name__ == '__main__':
    unittest.main()
