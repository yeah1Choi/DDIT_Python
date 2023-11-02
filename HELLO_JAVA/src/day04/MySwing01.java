package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextArea;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.ActionEvent;
import javax.swing.JTextPane;
import javax.swing.JLabel;
import java.awt.event.MouseEvent;

public class MySwing01 extends JFrame {

	private JPanel pan;
	JLabel lbl;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MySwing01 frame = new MySwing01();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public MySwing01() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		pan = new JPanel();
		pan.setBorder(new EmptyBorder(5, 5, 5, 5));

		setContentPane(pan);
		pan.setLayout(null);
		
		JButton btn = new JButton("Click");
		btn.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				myClick();
			}
		});
		
		btn.setBounds(224, 103, 97, 23);
		pan.add(btn);
		
		lbl = new JLabel("Good morning");
		lbl.setBounds(109, 107, 91, 15);
		pan.add(lbl);
	}
	void myClick() {
		lbl.setText("Good Evening");
	}
}
