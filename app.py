from dash import Dash, html, dcc, Input, Output, State
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import random

external_stylesheets = [
    'https://codepen.io/MarcoGuglielmelli/pen/ExGYae',
    'https://fonts.googleapis.com/css2?family=Bubblegum+Sans&display=swap'
]

app = Dash(__name__, external_stylesheets=external_stylesheets)

# Function to generate random star animation
def generate_stars():
    return [html.Div(
        id='star-' + str(i),
        className='star',
        style={'position': 'absolute',
               'backgroundColor': 'white',
               'borderRadius': '50%',
               'width': '4px',
               'height': '4px',
               'left': str(random.randint(0, 100)) + '%',
               'top': str(random.randint(0, 100)) + '%',
               'animation': 'twinkle ' + str(random.uniform(1, 3)) + 's linear infinite',
               'animation-delay': str(random.uniform(0, 3)) + 's'}
    ) for i in range(100)]

app.layout = html.Div(
    style={'position': 'relative', 'backgroundColor': 'black', 'color': 'white', 'height': '160vh', 'fontFamily': 'Bubblegum Sans'},
    children=[
        html.Div(
            id='stars-container',
            style={'position': 'absolute', 'width': '100%', 'height': '100%'},
            children=generate_stars()
        ),
        html.Div(
            style={'position': 'absolute', 'top': '50%', 'left': '50%', 'transform': 'translate(-50%, -50%)'},
            children=[
                html.H1(children='WELCOME TO MOOD BOOSTER', style={'textAlign': 'center'}),
                html.Div(
                    style={'textAlign': 'center'},
                    children=[
                        html.H3("How are you feeling today?", style={'marginBottom': 40}),
                        dcc.RadioItems(
                            id='mood-selector',
                            options=[
                                {'label': '😊 Happy', 'value': 'happy'},
                                {'label': '😔 Sad', 'value': 'sad'},
                                {'label': '😡 Angry', 'value': 'angry'},
                                {'label': '😴 Tired', 'value': 'tired'}
                            ],
                            style={'display': 'inline-block'},
                            labelStyle={'marginRight': '15px'}
                        ),
                        html.Div(id='output-message', style={'marginTop': 30}),
                        html.Button('GET A MOOD BOOST', id='mood-boost-button', n_clicks=0,
                                    style={'marginTop': 20, 'backgroundColor': '#4B0082', 'color': 'white',
                                           'borderRadius': '5px', 'padding': '10px 20px', 'fontSize': '20px'}),
                        html.Button("START BREATHING EXERCISE", id="start-breathing-button",
                                    style={'marginTop': 20, 'backgroundColor': '#4B0082', 'color': 'white',
                                           'borderRadius': '5px', 'padding': '10px 20px', 'fontSize': '20px'}),
                        dcc.Interval(id='breathing-interval', interval=1000, n_intervals=0, max_intervals=0),
                        html.Div(id="breathing-exercise",
                                 style={"textAlign": "center", "marginTop": "30px", "fontSize": "48px",
                                        "width": "800px"}),
                        dcc.Store(id='button-state', data={'n_clicks': 0, 'completed': False}),
                    ]
                ),
                html.Div(id='mood-gif', style={'marginTop': 20}),
                dcc.Dropdown(
                    id='astrological-sign',
                    options=[
                        {'label': 'Aries', 'value': 'Aries'},
                        {'label': 'Taurus', 'value': 'Taurus'},
                        {'label': 'Gemini', 'value': 'Gemini'},
                        {'label': 'Cancer', 'value': 'Cancer'},
                        {'label': 'Leo', 'value': 'Leo'},
                        {'label': 'Virgo', 'value': 'Virgo'},
                        {'label': 'Libra', 'value': 'Libra'},
                        {'label': 'Scorpio', 'value': 'Scorpio'},
                        {'label': 'Sagittarius', 'value': 'Sagittarius'},
                        {'label': 'Capricorn', 'value': 'Capricorn'},
                        {'label': 'Aquarius', 'value': 'Aquarius'},
                        {'label': 'Pisces', 'value': 'Pisces'},
                    ],
                    placeholder="Select your astrological sign",
                    style={'fontSize': '24px','width': '70%', 'margin': 'auto', 'marginTop': '20px', 'fontFamily': 'Bubblegum Sans',
                           'color': 'black'}
                ),
                html.Div(id='astrology-analysis', style={'fontSize': '24px','marginTop': 30})
            ]
        ),
        # Positioning Mental Health Resources button on the top right corner
        html.Div(
            id='resource-button-container',
            style={'position': 'absolute', 'top': '20px', 'right': '20px'},
            children=[
                html.Button('MENTAL HEALTH RESOURCES', id='resource-button', n_clicks=0, style={'backgroundColor': '#4B0082', 'color': 'white', 'borderRadius': '5px', 'padding': '10px 20px', 'fontSize': '20px'})
            ]
        ),
        html.Div(
            id='resource-modal',
            style={'position': 'fixed', 'top': '0', 'left': '0', 'width': '100%', 'height': '100%', 'backgroundColor': 'rgba(0,0,0,0.5)', 'display': 'none'},
            children=[
                html.Div(
                    style={'position': 'absolute', 'top': '50%', 'left': '50%', 'transform': 'translate(-50%, -50%)', 'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px'},
                    children=[
                        html.H2("MENTAL HEALTH RESOURCES", style={'textAlign': 'center', 'fontSize': '32px'}),


                        html.Ul([
                            html.Li(html.A("UIC Counseling", href="https://counseling.uic.edu", target="_blank")),
                            html.Li(html.A("National Alliance on Mental Illness (NAMI)", href="https://www.nami.org/", target="_blank")),
                            html.Li(html.A("National Suicide Prevention Lifeline", href="https://suicidepreventionlifeline.org/", target="_blank")),
                            html.Li(html.A("Crisis Text Line", href="https://www.crisistextline.org/", target="_blank")),
                            html.Li(html.A("MentalHealth.gov", href="https://www.mentalhealth.gov/", target="_blank")),
                            html.Li(html.A("Support Group", href="https://counseling.uic.edu/group-3/", target="_blank")),


                        ]),
                        html.Button("Close", id="close-modal-button", style={'marginTop': '20px', 'backgroundColor': '#FF4500', 'color': 'white', 'borderRadius': '5px', 'padding': '10px 20px', 'fontSize': '20px'})
                    ]
                )
            ]
        )
    ]
)

# Callback to toggle display of the resource modal
@app.callback(
    Output('resource-modal', 'style'),
    [Input('resource-button', 'n_clicks'),
     Input('close-modal-button', 'n_clicks')],
    [State('resource-modal', 'style')]
)
def toggle_modal(resource_clicks, close_clicks, modal_style):
    resource_clicks = resource_clicks or 0
    close_clicks = close_clicks or 0

    if resource_clicks > close_clicks:
        modal_style['display'] = 'block'
    else:
        modal_style['display'] = 'none'
    return modal_style

# Callback to display mood-specific message
@app.callback(
    Output('output-message', 'children'),
    [Input('mood-selector', 'value')]
)
def display_message(selected_mood):
    if selected_mood:
        if selected_mood == 'happy':
            return html.Div ("If life gives you lemons, make lemonade... then find someone whose life gave them vodka and have a party!", style={'fontSize': '25px'})
        elif selected_mood == 'sad':
            return html.Div("Why did the tomato turn red? Because it saw the salad dressing! Cheer up, laughter is the best salad dressing for the soul",style={'fontSize': '25px'})
        elif selected_mood == 'angry':
            return html.Div("Why was the math book sad? Because it had too many problems! Take a breather, let's turn those math problems into math puns", style={'fontSize': '25px'})
        elif selected_mood == 'tired':
            return html.Div("Why did the bicycle fall over? Because it was two-tired! Time for some well-deserved rest, you've earned it",style={'fontSize': '25px'})

# Callback to display mood-specific GIF
@app.callback(
    Output('mood-gif', 'children'),
    [Input('mood-boost-button', 'n_clicks')]
)
def display_image(n_clicks):
    image_urls = [
        'https://i0.wp.com/katzenworld.co.uk/wp-content/uploads/2019/06/funny-cat.jpeg?w=1920&ssl=1',
        'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9kwBk9683qTfDEXMPg1eL7O_GjXuwawh6KR_uXsVMsXQsr_EASeS9nqgz_tave1lTrTc&usqp=CAU',
        'https://i.pinimg.com/736x/ba/92/7f/ba927ff34cd961ce2c184d47e8ead9f6.jpg',
    ]

    if n_clicks > 0:
        # Select a random image URL from the list
        image_url = random.choice(image_urls)

        return html.Div(
            html.Img(src=image_url, style={'width': '30%', 'height': '30%', 'borderRadius': '8px'}),
            style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center', 'height': '100%'}
        )

# Change the ID of the "Start Breathing Exercise" button for the breathing exercise callback
@app.callback(
    [Output("breathing-exercise", "children"),
     Output("breathing-interval", "max_intervals"),
     Output("button-state", "data")],
    [Input("start-breathing-button", "n_clicks"),
     Input("breathing-interval", "n_intervals")],
    [State('button-state', 'data'),
     State('breathing-exercise', 'children')]
)
def update_breathing_exercise(n_clicks, n_intervals, button_state, current_text):
    if n_clicks is None:
        raise PreventUpdate

    ctx = dash.callback_context
    triggered_id = ctx.triggered_id if ctx.triggered_id else "start-breathing-button"

    if triggered_id == "start-breathing-button" and not button_state['completed']:
        return "Inhale!", 6, {'n_clicks': n_clicks, 'completed': False}

    elif triggered_id == "breathing-interval":
        inhale_duration = 6
        exhale_duration = 6
        total_duration = inhale_duration + exhale_duration

        elapsed_time = n_intervals % total_duration

        if elapsed_time < inhale_duration:
            return f"Inhale! {inhale_duration - elapsed_time}", total_duration, button_state
        elif elapsed_time == total_duration:
            if button_state['completed']:
                return "Breathing exercise completed!", 6, button_state
            else:
                return "Exhale!", 6, {'n_clicks': 0, 'completed': True}
        else:
            return "Exhale!", total_duration, button_state

# Callback to reset button state and timer
@app.callback(
    [Output("start-breathing-button", "n_clicks"),
     Output("breathing-interval", "n_intervals")],
    [Input("start-breathing-button", "n_clicks")],
    [State('button-state', 'data')]
)
def reset_button_state(n_clicks, button_state):
    if n_clicks and (button_state['completed'] or button_state['n_clicks'] == 0):
        return 0, 0
    raise PreventUpdate

# Callback to provide astrology-based mood analysis
@app.callback(
    Output('astrology-analysis', 'children'),
    [Input('mood-selector', 'value'), Input('astrological-sign', 'value')]
)
def display_astrology_analysis(selected_mood, astro_sign):
    astrology_messages = {
        'Aries': {
            'happy': "Feeling happy, Aries? Embrace your positive energy and take on the day with enthusiasm!",
            'sad': "Feeling sad, Aries? Remember, tough times don't last forever. Reach out to loved ones for support.",
            'angry': "Feeling angry, Aries? Take a deep breath and find healthy ways to express your emotions.",
            'tired': "Feeling tired, Aries? It's okay to rest and recharge. Listen to your body's needs."
        },
        'Taurus': {
            'happy': "Feeling happy, Taurus? Enjoy the simple pleasures in life and indulge in some self-care.",
            'sad': "Feeling sad, Taurus? Take some time to reflect on your emotions and seek comfort from loved ones.",
            'angry': "Feeling angry, Taurus? Channel your energy into productive activities and find constructive outlets.",
            'tired': "Feeling tired, Taurus? Treat yourself to some relaxation and unwind from your daily responsibilities."
        },
        'Gemini': {
            'happy': "Feeling happy, Gemini? Your quick wit and adaptability make every moment an adventure!",
            'sad': "Feeling sad, Gemini? Allow yourself to acknowledge your emotions and seek out activities that bring you joy.",
            'angry': "Feeling angry, Gemini? Use your communication skills to express your feelings constructively and find resolutions.",
            'tired': "Feeling tired, Gemini? Take a break and explore activities that stimulate your curious mind without draining your energy."
        },
        'Cancer': {
            'happy': "Feeling happy, Cancer? Your nurturing nature brings warmth and joy to those around you. Embrace the love that surrounds you!",
            'sad': "Feeling sad, Cancer? Allow yourself to express your emotions and lean on your close-knit circle of loved ones for support.",
            'angry': "Feeling angry, Cancer? Your sensitivity runs deep, but remember to assert your boundaries and express your feelings calmly.",
            'tired': "Feeling tired, Cancer? Retreat into the comfort of your home and recharge your emotional batteries with some self-care and relaxation."
        },
        'Leo': {
            'happy': "Feeling happy, Leo? Your confidence and charisma light up any room. Shine bright like the star you are!",
            'sad': "Feeling sad, Leo? Remember that vulnerability is a strength. Reach out to your loyal friends for comfort and support.",
            'angry': "Feeling angry, Leo? Channel your passion into productive outlets and lead with courage and integrity.",
            'tired': "Feeling tired, Leo? Take a step back and recharge your energy. Remember to listen to your body's needs."
        },
        'Virgo': {
            'happy': "Feeling happy, Virgo? Your attention to detail and dedication to improvement bring you satisfaction and fulfillment.",
            'sad': "Feeling sad, Virgo? It's okay to feel overwhelmed at times. Take a break and focus on self-care and organization.",
            'angry': "Feeling angry, Virgo? Your analytical mind seeks solutions. Use your intellect to address the source of your frustration.",
            'tired': "Feeling tired, Virgo? Remember to prioritize rest and relaxation. Set aside time for yourself to recharge and rejuvenate."
        },
        'Libra': {
            'happy': "Feeling happy, Libra? Your sense of harmony and fairness brings joy to those around you. Embrace the beauty of balance!",
            'sad': "Feeling sad, Libra? Your empathy allows you to deeply connect with others' emotions. Reach out for support and find solace in your relationships.",
            'angry': "Feeling angry, Libra? Your diplomacy and tact can help you navigate conflicts with grace. Seek compromise and understanding.",
            'tired': "Feeling tired, Libra? Remember to prioritize self-care and find moments of tranquility amidst life's demands."
        },
        'Scorpio': {
            'happy': "Feeling happy, Scorpio? Your intensity and passion make every triumph feel exhilarating. Embrace the depth of your emotions!",
            'sad': "Feeling sad, Scorpio? Your resilience allows you to rise from the depths of despair. Trust in your inner strength and seek support when needed.",
            'angry': "Feeling angry, Scorpio? Your determination fuels your drive for justice. Use your power wisely and transform anger into positive action.",
            'tired': "Feeling tired, Scorpio? Remember to honor your need for solitude and introspection. Embrace the healing power of rest and reflection."
        },
        'Sagittarius': {
            'happy': "Feeling happy, Sagittarius? Your optimism and adventurous spirit brighten every journey. Embrace new experiences and spread joy!",
            'sad': "Feeling sad, Sagittarius? Your philosophical nature allows you to find meaning even in difficult times. Seek wisdom and perspective.",
            'angry': "Feeling angry, Sagittarius? Your honesty and directness cut through confusion. Channel your passion into positive change.",
            'tired': "Feeling tired, Sagittarius? Remember to recharge your adventurous soul with moments of relaxation and inner exploration."
        },
        'Capricorn': {
            'happy': "Feeling happy, Capricorn? Your disciplined approach brings success and fulfillment. Celebrate your achievements and keep striving for excellence!",
            'sad': "Feeling sad, Capricorn? Your resilience and determination guide you through challenges. Trust in your abilities and lean on your support system.",
            'angry': "Feeling angry, Capricorn? Your practicality and patience help you overcome obstacles. Stay focused on your goals and maintain your composure.",
            'tired': "Feeling tired, Capricorn? Remember to honor your need for rest and recuperation. Balance hard work with moments of relaxation and rejuvenation."
        },
        'Aquarius': {
            'happy': "Feeling happy, Aquarius? Your innovative mind and humanitarian spirit inspire positive change. Keep sharing your unique perspective with the world!",
            'sad': "Feeling sad, Aquarius? Your compassionate nature allows you to empathize deeply with others. Reach out for support and remember that your emotions are valid.",
            'angry': "Feeling angry, Aquarius? Your progressive ideals drive you to fight for justice and equality. Channel your energy into constructive activism.",
            'tired': "Feeling tired, Aquarius? Remember to take breaks and nurture your creative spark. Your imagination thrives when you give yourself space to dream."
        },
        'Pisces': {
            'happy': "Feeling happy, Pisces? Your intuitive nature and empathetic heart bring joy to those around you. Embrace the beauty of the present moment and share your love with others!",
            'sad': "Feeling sad, Pisces? Your sensitive soul feels deeply, but remember that your emotions ebb and flow like the tides. Allow yourself to feel, and trust that brighter days are ahead.",
            'angry': "Feeling angry, Pisces? Your compassionate spirit seeks harmony, even in moments of conflict. Find peaceful outlets for your emotions and seek understanding.",
            'tired': "Feeling tired, Pisces? Your imaginative mind needs moments of quiet reflection to recharge. Allow yourself to escape into creativity and reconnect with your inner world."
        },
    }
    if selected_mood and astro_sign:
        astrology_message = astrology_messages.get(astro_sign, {}).get(selected_mood, "Your astrological sign does not have specific mood analysis for this level.")
        return html.P(astrology_message, style={'textAlign': 'center','fontFamily': 'Bubblegum Sans', 'marginLeft': '20px'})

if __name__ == '__main__':
        app.run_server(debug=True)
