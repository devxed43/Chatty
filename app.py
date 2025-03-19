
# Greet your customer and introduce the ChatBot.
print("")
print("💥 Hello friend! 💥, how are you? I'm Chatty 🤖")

# Before starting the "conversation" ask the user if they would like to learn more about a specific product or service. If they say yes, proceed to tell them about your product or service. If they say no, end the conversation and provide a farewell.
learn_more = input("Is there anything you'd like to learn more about today? Y/N: ")
print()
print("====================================================================")
print()

if learn_more == 'y' or learn_more == 'Y' or learn_more == "product" or learn_more == "service":
    print("💡 We are an AI company but we like to think of ourselves as companions. \n \n We take smart devices and make them smarter. \n \n Our biggest seller is our phone. \n \n Equipped with features that free up time and energy for our customers rather than weigh them down with more and more selling and tracking. \n \n We believe in doing the work of allowing our customers to live a more freedom filled life to the point where they don't need us. \n \n That's how they know we are doing our job. \n \n At the end of each night, we silently send a report on what we noticed throughout the day and what we assisted with. \n \n We only improve as our customers lives improve. That's it!\n")

    print()
    print("====================================================================")
    print()

    # Build this chat conversation around a specific product or service. Provide a paragraph overview of your product or service. Be creative - make some stuff up. Have a fun and engaging "conversation" with your user. Output the overview to the screen with a nice formatting of your choice - for example, break up a long overview into multiple lines. Make this as serious or as silly a scenario as you want it to be. This is an important step to "SELL" the product or service.
    product = input("would you like to learn more about our phone? ")
    print()
    print("====================================================================")
    print()

    if product == "Y" or product == "y" or product == "yes":
        print("ChatPhone has a lot of cool features like built-in spam blocking so you don't recieve annoying spam calls as well as protecting you from targeted social media marketing ads so you can have more of your time back.")
        print()
        print("====================================================================")
        print()
        bot = input("Does ChatPhone interest you? Y/N: ")
        print()

        if bot == "Y" or  bot == "y" or bot == "yes":
            print("you have a few options! we have: \n 💰 low tier, \n 💰💰 mid tier \n 💰💰💰 high tier \n so you can buy what is right for your wallet. \n we don't believe in breaking the bank so we also have payment plan options with low interest rates. \n A companion should be something we all have, not just those who can afford the most expensive option.")
            
            print()
            print("====================================================================")
            print()
            tier = input("which tier are you thinking of choosing? ")
            print()

            if tier == "low" or tier == "low tier":
                print("$600 range is considered the economical choice with all standard features and a month free of spotify")
            elif tier == "mid" or tier == "mid tier":
                print("The mid tier is $750. Standard features and comes with Netflix")
            elif tier == "high" or tier == "high tier":
                print("The higher tier is $1200. You get more storage, better camera resolution and more control over your companion")
            else: 
                print("please choose a tier")

            print()
            print("====================================================================")
            print()    


            # Ask if the user would be interested in purchasing your product or service. Build this around an if statement. If yes - continue with the sales conversation. If no, provide a closing statement and farewell.
            purchase = input("Do you want to go ahead and buy the phone? \n \n")
          
            # Shopping Cart Final Stage
            if purchase == "y" or purchase == "Y" or purchase == "yes":
                print(f"you have chosen the {tier} tier 😁")

                print()

                print("before we finalize your order, please provide the following information")
                print("====================================================================")
                
                # Ask for the customer's first and last name. Store the values input to separate variables such as firstName and lastName.
                first_name = str(input("enter first name: "))
                print("====================================================================")
                last_name = str(input("enter last name: "))
                print("====================================================================")
                
                # Ask for their email address. Store the value input to a variable. Don't worry about validating the format of the input.
                email = str(input("enter email address: "))
                print("====================================================================")
                
                # Ask for their phone number.  Store the value input to a variable. Don't worry about enforcing formatting on the input. 
                phone = int(input("enter phone number: "))
                print("====================================================================")
                # Ask for how many of the product/service they would like to purchase. Be sure to tell the customer how much the product/service
                quantity = int(input("how many phones do you want to buy? "))
                print()

                # costs BEFORE asking how many they would like to purchase. Store the values input to a variable.
                subtotal = quantity * 1200
                # Apply 10% tax for the total bill. 
                tax = 1.10
                total = (subtotal * tax)
                
                # Calculate and display their current total based on the quantity they would like to purchase. Store the values input to a variable.
                print(f"sub total: ${subtotal}")
                print()

                # Calculate the total amount due (the total + tax). Store the values input to a variable. Output the total amount due before proceeding to the next step.
                print(f"total: ${total}")

                print("====================================================================")
                print()
                confirm_purchase = input("confirm purchase? ")
                # Output a receipt using all of the variables you have input. Be sure to show the total product/service quantity, the cost for each product/service, the subtotal, tax, and total amount due. Format this as nice as you can - use symbols and line breaks to produce a realistic looking receipt.
                subtotal = quantity * 1200
                tax = 1.10
                total = (subtotal * tax)
                if confirm_purchase == "y" or confirm_purchase == "Y" or confirm_purchase == "yes":
                    confirm_purchase = input("are you sure? ")
                    print()
                    print("====================================================================")
                    # In the receipt output, include the customer's name, phone number, and email address.  Format this as nice as you can - use symbols and line breaks to produce a realistic looking receipt.
                    print(f"✨✨✨ \n Receipt: \n {first_name} {last_name}, \n you ordered {quantity} ChatPhones \n subtotal: ${subtotal} \n total: ${total} \n✨✨✨")
                    print("====================================================================")
                    print()
                    # Output a farewell and a thank you to the customer. 
                    print("Thank you for shopping with us! We value your business with us more than anything")
                else:
                    print("have a good day!")
            elif purchase == "n" or purchase == "N" or purchase == "no":
                print("maybe next time then!")
            else:
                print("Invalid entry")
else:
    print("have a nice day")