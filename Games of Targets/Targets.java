import java.util.*;
import java.applet.*;
import java.awt.*;
import java.awt.event.*;

public class Targets extends Applet
{
	Graphics gfx;
	int score1, score2;
	int x1, y1, x2, y2; 
	int refX= 30, refY = 30;
	Color clr1 = Color.red;
	Color clr2 = Color.blue;
	int step = 5;  // step in pixel
	int ht = 20;  // height (thickness ) of score bar
	int maxScore = 500/step;
	
	boolean f1 , f2;  // for checking hit
	
	Button btn1 = new Button("PLAYER: 1");
	Button btn2 = new Button("PLAYER: 2");
	Button btnstart = new Button("START");
	Label scr1 = new Label("0");
	Label scr2 = new Label("0");
	
	public void init()
	{
		setLayout(null);
		btn1.setBounds( refX+60, 300+10, 90, 30 );
		scr1.setBounds( refX+60+100, 300+10, 40,30);
		add(btn1);
		add(scr1);
		btn2.setBounds( refX+200 +60 , 300+10, 90, 30 );
		scr2.setBounds( refX+200 +160 , 300+10, 40, 30 );
		add(btn2);
		add(scr2);
		btnstart.setBounds( refX+200+250, 300+10, 70, 30);
		add(btnstart);
		
		btn1.addActionListener( new BtnListener());
		btn2.addActionListener( new BtnListener());
		btnstart.addActionListener( new StartButton());
		
	}
	private void drawScreen(Graphics g)
	{
		
		y1 = refY + 100;
		y2 = refY + 200;
		
		// Outline of Game area
		g.setColor( Color.green );
		g.drawRect( refX, refY , 700, 400 );
		
		Font f = new Font("Arial", Font.BOLD, 12 );
		g.setFont(f);
		// Player 1 status
		g.setColor( clr1 );
		g.fillRoundRect(refX-5, y1 , 5+score1*step, ht,7,7 );
		g.drawString("Player 1 : " + score1 , refX+50, y1+ht+15);
		g.drawRect( refX+50, 300, 150, 50);
		
		// Player 2 status
		g.setColor( clr2 );
		g.fillRoundRect(refX-5, y2, 5+score2*step, ht,7,7 );
		g.drawString("Player 2 : " + score2 , refX+50, y2+ht+15);
		g.drawRect( refX+50 + 200, 300, 150, 50);

		// line throgh scorebars
		g.setColor(Color.black);
		g.drawLine( refX, y1+ht, refX +score1*step -5, y1+ht );
		g.drawLine( refX, y2+ht, refX +score2*step -5, y2+ht );
		g.setColor(Color.white);
		g.drawLine( refX, y1+5, refX +score1*step -5, y1+5 );
		g.drawLine( refX, y2+5, refX +score2*step -5, y2+5 );
		
		// show message if any player is hit
		g.setColor( Color.orange );
		if( f1 == true )
			g.drawString( "Payer - 1 was hit .. !",refX+150, y1+ht+25);
		else if( f2== true)
			g.drawString( "Payer - 2 was hit .. !",refX+150, y1+ht+25);
		//g.drawString( "Payer - 2 was hit .. !",refX+150, y1+ht+15);
		
		// plyaer wins
		if( score1 >= maxScore )
		{
			f = new Font("Arial", Font.BOLD, 16 );
			g.setColor(Color.red);
			g.setFont(f);
			g.drawString("Player 1 ... Wins ! ! !", 400, 400);
			btn1.setEnabled(false);
			btn2.setEnabled(false);
		}
		else if( score2 >= maxScore )
		{
			f = new Font("Arial", Font.BOLD, 16 );
			g.setColor(Color.blue);
			g.setFont(f);
			g.drawString("Player 2 ... Wins ! ! !", 400, 400);
			btn1.setEnabled(false);
			btn2.setEnabled(false);
		}
		
	}
	public void paint( Graphics g )
	{
		gfx = g;
		setLayout(null);
		drawScreen(g);
		g.setFont( new Font("Arial", Font.BOLD, 20 ));
		g.setColor(Color.green);
		g.drawString("| Game of Targets |", 200, 60);
	}
	
	class BtnListener implements ActionListener
	{
		public void actionPerformed(ActionEvent ev )
		{
			f1 = f2 = false;
			int v;
			Random rnd = new Random();
			v = rnd.nextInt(6);
			if( v == 0 )
				v = 1;
				
			String s = ev.getActionCommand();
			if( s.endsWith("1"))
			{
				scr1.setText( v+"");
				scr2.setText("-");
				btn1.setEnabled(false);
				btn2.setEnabled(true);
				score1 += v;
				if( score1 == score2 )
				{
					f2 = true;
					if( score2 > 5 )
						score2 -= 5;
					else
						score2 = 0;
				}
					
			}
			else if( s.endsWith("2"))
			{
				scr1.setText( "-");
				scr2.setText(v+ "");
				btn1.setEnabled(true);
				btn2.setEnabled(false);
				score2 += v;
				if( score2 == score1 )
				{
					f1 = true;
					if( score1 > 5 )
						score1 -= 5;
					else
						score1 = 0;
				}
			}
			repaint();
		}	
	}
	




	class StartButton implements ActionListener
	{
		public void actionPerformed(ActionEvent ev )
		{
			scr1.setText("0");
			scr2.setText("0");
			score1=score2=0;
			f1=f2=false;
			btn1.setEnabled(true);
			btn2.setEnabled(true);
			repaint();
		}
		
	}
}
