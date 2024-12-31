import json

booklist = """
  {
    "itemsList": [
        {
            "asin": "B09BNH4TLW",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB09BNH4TLW",
            "productUrl": "https://m.media-amazon.com/images/I/51fMaH1tRyL._SY400_.jpg",
            "title": "Remarkably Bright Creatures: A Novel",
            "percentageRead": 0,
            "authors": [
                "Van Pelt, Shelby:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B08FK7MVPF",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB08FK7MVPF",
            "productUrl": "https://m.media-amazon.com/images/I/511kwc1jkxL._SY400_.jpg",
            "title": "Mary Jane: A Novel",
            "percentageRead": 0,
            "authors": [
                "Blau, Jessica Anya:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B092T8L15J",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB092T8L15J",
            "productUrl": "https://m.media-amazon.com/images/I/5135mAAiLVL._SY400_.jpg",
            "title": "Little Souls: A Novel",
            "percentageRead": 0,
            "authors": [
                "Dallas, Sandra:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B00630NYTU",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB00630NYTU",
            "productUrl": "https://m.media-amazon.com/images/I/51WPh6XSl3L._SY400_.jpg",
            "title": "Double Fudge (Fudge series Book 5)",
            "percentageRead": 0,
            "authors": [
                "Blume, Judy:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B00K0OI42W",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB00K0OI42W",
            "productUrl": "https://m.media-amazon.com/images/I/51p12agL5LL._SY400_.jpg",
            "title": "To Kill a Mockingbird (Harperperennial Modern Classics)",
            "percentageRead": 0,
            "authors": [
                "Lee, Harper:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B08G1NJK2R",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB08G1NJK2R",
            "productUrl": "https://m.media-amazon.com/images/I/51Xbu8vnX7L._SY400_.jpg",
            "title": "The Cartographers: A Novel",
            "percentageRead": 0,
            "authors": [
                "Shepherd, Peng:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B09QMHZ53K",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB09QMHZ53K",
            "productUrl": "https://m.media-amazon.com/images/I/510+1V2S8oL._SY400_.jpg",
            "title": "Demon Copperhead: A Novel",
            "percentageRead": 0,
            "authors": [
                "Kingsolver, Barbara:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B072B86YSS",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB072B86YSS",
            "productUrl": "https://m.media-amazon.com/images/I/51nzCWGobnL._SY400_.jpg",
            "title": "The Country Girls: Three Novels and an Epilogue: (The Country Girl; The Lonely Girl; Girls in Their Married Bliss; Epilogue) (FSG Classics)",
            "percentageRead": 0,
            "authors": [
                "O\u0027Brien, Edna:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B01N979PNC",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB01N979PNC",
            "productUrl": "https://m.media-amazon.com/images/I/41cZKBgxCiL._SY400_.jpg",
            "title": "Blonde: A Novel",
            "percentageRead": 0,
            "authors": [
                "Oates, Joyce Carol:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B09BV2JNWV",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB09BV2JNWV",
            "productUrl": "https://m.media-amazon.com/images/I/414Nfj4Ea9L._SY400_.jpg",
            "title": "Trust (Pulitzer Prize Winner)",
            "percentageRead": 0,
            "authors": [
                "Diaz, Hernan:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B0BTX6JH7S",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB0BTX6JH7S",
            "productUrl": "https://m.media-amazon.com/images/I/41Ql5vz+oTL._SY400_.jpg",
            "title": "Absolution: A Novel",
            "percentageRead": 0,
            "authors": [
                "McDermott, Alice:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B07T693397",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB07T693397",
            "productUrl": "https://m.media-amazon.com/images/I/41+2tArGYCL._SY400_.jpg",
            "title": "Maggie-Now: A Novel",
            "percentageRead": 0,
            "authors": [
                "Smith, Betty:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B0C7TNRTQZ",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB0C7TNRTQZ",
            "productUrl": "https://m.media-amazon.com/images/I/51qDNckATTL._SY400_.jpg",
            "title": "The Underground Library: A Novel",
            "percentageRead": 0,
            "authors": [
                "Ryan, Jennifer:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B000FC1COG",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB000FC1COG",
            "productUrl": "https://m.media-amazon.com/images/I/41ApPQCZMXL._SY400_.jpg",
            "title": "Poems of Emily Dickinson Series One",
            "percentageRead": 0,
            "authors": [
                "Dickinson, Emily:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B07P1PSX3D",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB07P1PSX3D",
            "productUrl": "https://m.media-amazon.com/images/I/515bXXZmfHL._SY400_.jpg",
            "title": "The Confession Club: A Novel (Mason Book 3)",
            "percentageRead": 0,
            "authors": [
                "Berg, Elizabeth:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B0012E3J60",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB0012E3J60",
            "productUrl": "https://m.media-amazon.com/images/I/51poAD+37OL._SY400_.jpg",
            "title": "The Accidental Tourist: A Novel",
            "percentageRead": 0,
            "authors": [
                "Tyler, Anne:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B003N9BELY",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB003N9BELY",
            "productUrl": "https://m.media-amazon.com/images/I/51eNtMXnrWL._SY400_.jpg",
            "title": "Terms of Endearment: A Novel (Houston Book 3)",
            "percentageRead": 0,
            "authors": [
                "McMurtry, Larry:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B0030P1WSG",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB0030P1WSG",
            "productUrl": "https://m.media-amazon.com/images/I/51Uk53smqcL._SY400_.jpg",
            "title": "Summer Sisters: A Novel",
            "percentageRead": 0,
            "authors": [
                "Blume, Judy:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B015VACH4U",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB015VACH4U",
            "productUrl": "https://m.media-amazon.com/images/I/41otqMcqCjL._SY400_.jpg",
            "title": "Homegoing: A novel",
            "percentageRead": 0,
            "authors": [
                "Gyasi, Yaa:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B000FC1KN4",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB000FC1KN4",
            "productUrl": "https://m.media-amazon.com/images/I/41t1CxxQ8NL._SY400_.jpg",
            "title": "Tepper Isn\u0027t Going Out: A Novel",
            "percentageRead": 0,
            "authors": [
                "Trillin, Calvin:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B000SEGZRK",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB000SEGZRK",
            "productUrl": "https://m.media-amazon.com/images/I/51lFVcK4xtL._SY400_.jpg",
            "title": "Harriet the Spy",
            "percentageRead": 0,
            "authors": [
                "Fitzhugh, Louise:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B07PRXT94R",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB07PRXT94R",
            "productUrl": "https://m.media-amazon.com/images/I/51YP8NqVZ9L._SY400_.jpg",
            "title": "The Dutch House: A Novel",
            "percentageRead": 0,
            "authors": [
                "Patchett, Ann:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B000FC14BW",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB000FC14BW",
            "productUrl": "https://m.media-amazon.com/images/I/51GS0BWMJzL._SY400_.jpg",
            "title": "Unless: A Novel (P.S.)",
            "percentageRead": 0,
            "authors": [
                "Shields, Carol:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B006VGG37Q",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB006VGG37Q",
            "productUrl": "https://m.media-amazon.com/images/I/51S829N1r7L._SY400_.jpg",
            "title": "The Quilter\u0027s Apprentice: A Novel (The Elm Creek Quilts Book 1)",
            "percentageRead": 0,
            "authors": [
                "Chiaverini, Jennifer:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B001RO6P7U",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB001RO6P7U",
            "productUrl": "https://m.media-amazon.com/images/I/517nSNJO0-L._SY400_.jpg",
            "title": "The Courtier and the Heretic: Leibniz, Spinoza, and the Fate of God in the Modern World",
            "percentageRead": 0,
            "authors": [
                "Stewart, Matthew:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B09FLR5W3H",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB09FLR5W3H",
            "productUrl": "https://m.media-amazon.com/images/I/51VQFciOjyL._SY400_.jpg",
            "title": "The Littlest Library: A Novel",
            "percentageRead": 0,
            "authors": [
                "Alexander, Poppy:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B0BQLVTBYZ",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB0BQLVTBYZ",
            "productUrl": "https://m.media-amazon.com/images/I/51muX9XFuZL._SY400_.jpg",
            "title": "Night Watch (Pulitzer Prize Winner): A novel",
            "percentageRead": 0,
            "authors": [
                "Phillips, Jayne Anne:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B004GTLKLY",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB004GTLKLY",
            "productUrl": "https://m.media-amazon.com/images/I/51rFat3BAAL._SY400_.jpg",
            "title": "Breathing Lessons: A Novel",
            "percentageRead": 0,
            "authors": [
                "Tyler, Anne:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B004QZ9PE2",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB004QZ9PE2",
            "productUrl": "https://m.media-amazon.com/images/I/51Ik13iNM7L._SY400_.jpg",
            "title": "The Art of Fielding: A Novel",
            "percentageRead": 0,
            "authors": [
                "Harbach, Chad:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B01E7FUSU0",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB01E7FUSU0",
            "productUrl": "https://m.media-amazon.com/images/I/41fEgbmsogL._SY400_.jpg",
            "title": "Ironweed: Pulitzer Prize Winner (A Novel)",
            "percentageRead": 0,
            "authors": [
                "Kennedy, William:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B001ANURFO",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB001ANURFO",
            "productUrl": "https://m.media-amazon.com/images/I/41TDlkzV3BL._SY400_.jpg",
            "title": "A Mercy",
            "percentageRead": 0,
            "authors": [
                "Morrison, Toni:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B0013TRR80",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB0013TRR80",
            "productUrl": "https://m.media-amazon.com/images/I/41pmiC-0GrL._SY400_.jpg",
            "title": "Olive Kitteridge: Fiction",
            "percentageRead": 0,
            "authors": [
                "Strout, Elizabeth:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B0063629YK",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB0063629YK",
            "productUrl": "https://m.media-amazon.com/images/I/51syki73TBL._SY400_.jpg",
            "title": "Tales of a Fourth Grade Nothing (Fudge Series Book 1)",
            "percentageRead": 0,
            "authors": [
                "Blume, Judy:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B007EDY9D0",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB007EDY9D0",
            "productUrl": "https://m.media-amazon.com/images/I/51IkqT3V9UL._SY400_.jpg",
            "title": "Bodily Harm (A Romance Bestseller)",
            "percentageRead": 0,
            "authors": [
                "Atwood, Margaret:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B00EMXBDMA",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB00EMXBDMA",
            "productUrl": "https://m.media-amazon.com/images/I/31hEtQyGIVL._SY400_.jpg",
            "title": "The Martian: A Novel",
            "percentageRead": 0,
            "authors": [
                "Weir, Andy:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B002KP6DXQ",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB002KP6DXQ",
            "productUrl": "https://m.media-amazon.com/images/I/51httki9EbL._SY400_.jpg",
            "title": "Artemis Fowl",
            "percentageRead": 0,
            "authors": [
                "Colfer, Eoin:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B0011UGMFU",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB0011UGMFU",
            "productUrl": "https://m.media-amazon.com/images/I/51MjzQv34dL._SY400_.jpg",
            "title": "Decked (A Regan Reilly Mystery Book 1)",
            "percentageRead": 0,
            "authors": [
                "Clark, Carol Higgins:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B007I5QMY8",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB007I5QMY8",
            "productUrl": "https://m.media-amazon.com/images/I/415PMcw3wIL._SY400_.jpg",
            "title": "Deenie",
            "percentageRead": 0,
            "authors": [
                "Blume, Judy:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B07TFB429F",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB07TFB429F",
            "productUrl": "https://m.media-amazon.com/images/I/41fBrxC2quL._SY400_.jpg",
            "title": "The Women in Black: A Novel",
            "percentageRead": 0,
            "authors": [
                "St John, Madeleine:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B0BWSJ98X1",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB0BWSJ98X1",
            "productUrl": "https://m.media-amazon.com/images/I/51ZBPzDdr7L._SY400_.jpg",
            "title": "The Great Gatsby: Original 1925 Edition (An F. Scott Fitzgerald Classic Novel)",
            "percentageRead": 0,
            "authors": [
                "Fitzgerald, F Scott:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B0084A7AAG",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB0084A7AAG",
            "productUrl": "https://m.media-amazon.com/images/I/51VRXtuf1nL._SY400_.jpg",
            "title": "One of Ours",
            "percentageRead": 0,
            "authors": [
                "Cather, Willa Sibert:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B07XCWSVLX",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB07XCWSVLX",
            "productUrl": "https://m.media-amazon.com/images/I/51F2cRcX4EL._SY400_.jpg",
            "title": "Invisible Man",
            "percentageRead": 0,
            "authors": [
                "Ellison, Ralph:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B00AFVEYRY",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB00AFVEYRY",
            "productUrl": "https://m.media-amazon.com/images/I/51VUbJF44PL._SY400_.jpg",
            "title": "The Fifties",
            "percentageRead": 0,
            "authors": [
                "Halberstam, David:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B01B1ZWUJG",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB01B1ZWUJG",
            "productUrl": "https://m.media-amazon.com/images/I/51D6ADBHf6L._SY400_.jpg",
            "title": "The Rainbow Trail: By Zane Grey : Illustrated",
            "percentageRead": 0,
            "authors": [
                "Zane Grey:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B00LYPFEZ6",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB00LYPFEZ6",
            "productUrl": "https://m.media-amazon.com/images/I/41+0aAZuNhL._SY400_.jpg",
            "title": "Riders of the Purple Sage (Illustrated)",
            "percentageRead": 0,
            "authors": [
                "Grey, Zane:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B09HR5FQRJ",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB09HR5FQRJ",
            "productUrl": "https://m.media-amazon.com/images/I/51aZjDZkecL._SY400_.jpg",
            "title": "A Room with a View (Warbler Classics Annotated Edition)",
            "percentageRead": 0,
            "authors": [
                "Forster, E. M.:Trilling, Lionel:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B00GQDOD80",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB00GQDOD80",
            "productUrl": "https://m.media-amazon.com/images/I/51YeA6LGQcL._SY400_.jpg",
            "title": "The Princess Bride: An Illustrated Edition of S. Morgenstern\u0027s Classic Tale of True Love and High Adventure",
            "percentageRead": 0,
            "authors": [
                "Goldman, William:Manomivibul, Michael:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B000O76NMS",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB000O76NMS",
            "productUrl": "https://m.media-amazon.com/images/I/51T21IFmiUL._SY400_.jpg",
            "title": "Gilead (Oprah\u0027s Book Club): A Novel",
            "percentageRead": 0,
            "authors": [
                "Robinson, Marilynne:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B006GR7JRS",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB006GR7JRS",
            "productUrl": "https://m.media-amazon.com/images/I/41CTxT2WS0L._SY400_.jpg",
            "title": "The Fixer: A Novel (FSG Classics)",
            "percentageRead": 0,
            "authors": [
                "Malamud, Bernard:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        },
        {
            "asin": "B009VR4U5Y",
            "webReaderUrl": "https://read.amazon.com/?asin\u003dB009VR4U5Y",
            "productUrl": "https://m.media-amazon.com/images/I/51l-YWN7qcL._SY400_.jpg",
            "title": "Imaginary Friends: A Novel",
            "percentageRead": 0,
            "authors": [
                "Lurie, Alison:"
            ],
            "resourceType": "EBOOK",
            "originType": "PURCHASE",
            "mangaOrComicAsin": false
        }
    ],
    "paginationToken": "48",
    "libraryType": "BOOKS",
    "sortType": "RECENCY"
}  
"""

books = json.loads(booklist)

for book in books["itemsList"]:
    print(f'{book["title"]}|{book["authors"][0]}')
