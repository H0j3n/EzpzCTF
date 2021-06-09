# Web

Challenge Name : Slot_Machines

# Solution

Open the link to the website will show us this page.

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210609152738.png)

The description of the challenge tell us to find a bug to get a reward/flag. View the `slotEngine.js`, we found out that it check if the `price` is more than `1000000000` we can get the flag.

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210609153123.png)

Let's check what is actually variable `price` . These are the lines related to `price`.  

```bash
var price = +($("#credits").text());

price = price + (bet*3);
price = price + (bet*2);
price = price - bet;
```

The price value will change depends on the bet value itself. Since we can manipulate the value of bet, let's try change that to become more than 1 billion. You can run this code in inspect element > console.
```code
document.getElementById("bets").innerHTML = "-100000000000000"
```

# Flag

![](https://github.com/H0j3n/EzpzCTF/blob/main/src/Pasted%20image%2020210609153809.png)


