"""empty message

Revision ID: ad2ad7082d2a
Revises: 9fa0234ffdc1
Create Date: 2023-10-28 23:07:42.469305

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'ad2ad7082d2a'
down_revision: Union[str, None] = '9fa0234ffdc1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('validator',
    sa.Column('username', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('username')
    )
    op.drop_table('TicketTimeFrame')
    op.drop_table('experience_ticket_classes')
    op.drop_table('PresentationType')
    op.drop_table('movie_genres')
    op.drop_table('experience_screening_resolutions')
    op.drop_table('ScreeningResolution')
    op.drop_table('TicketClass')
    op.drop_table('ScreeningFormat')
    op.drop_table('Auth0Identity')
    op.drop_table('MovieReview')
    op.drop_table('User')
    op.drop_table('experience_presentation_types')
    op.drop_table('PromoCodeUse')
    op.drop_table('user_followers')
    op.drop_table('InquiryTopic')
    op.drop_table('Faq')
    op.drop_table('user_favourites')
    op.drop_table('ScheduledMovie')
    op.drop_index('ix_CouponPurchase_order_id', table_name='CouponPurchase')
    op.drop_table('CouponPurchase')
    op.drop_table('CinemaReview')
    op.drop_table('Admin')
    op.drop_table('Cinema')
    op.drop_table('CouponSaleCatalog')
    op.drop_table('CinemaExperience')
    op.drop_table('experience_screening_formats')
    op.drop_table('user_watch_later')
    op.drop_index('ix_Movie_tmdb_id', table_name='Movie')
    op.drop_table('Movie')
    op.drop_table('PromoCode')
    op.drop_table('Inquiry')
    op.drop_table('Coupon')
    op.drop_table('Genre')
    op.drop_index('ix_apscheduler_jobs_next_run_time', table_name='apscheduler_jobs')
    op.drop_table('apscheduler_jobs')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('apscheduler_jobs',
    sa.Column('id', sa.VARCHAR(length=191), autoincrement=False, nullable=False),
    sa.Column('next_run_time', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('job_state', postgresql.BYTEA(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='apscheduler_jobs_pkey')
    )
    op.create_index('ix_apscheduler_jobs_next_run_time', 'apscheduler_jobs', ['next_run_time'], unique=False)
    op.create_table('Genre',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Genre_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('tmdb_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Genre_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('Coupon',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Coupon_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('coupon_sale_catalog_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_redeemed', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('redeemed_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('expires_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('is_expired', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('purchase_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['coupon_sale_catalog_id'], ['CouponSaleCatalog.id'], name='Coupon_coupon_sale_catalog_id_fkey'),
    sa.ForeignKeyConstraint(['purchase_id'], ['CouponPurchase.id'], name='Coupon_purchase_id_fkey', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name='Coupon_pkey')
    )
    op.create_table('Inquiry',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Inquiry_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('topic_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('contact_email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('message', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('is_answered', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['topic_id'], ['InquiryTopic.id'], name='Inquiry_topic_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], name='Inquiry_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='Inquiry_pkey')
    )
    op.create_table('PromoCode',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"PromoCode_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('code', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('discount', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PromoCode_pkey'),
    sa.UniqueConstraint('code', name='PromoCode_code_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('Movie',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Movie_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('tmdb_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('imdb_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('original_title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('adult', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('original_language', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('tagline', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('overview', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('release_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('runtime', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('trailer_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('poster_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('backdrop_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('cast', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('directors', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('writers', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('ratings', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('raters_count', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('tmdb_rating', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('tmdb_raters_count', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('budget', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Movie_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_Movie_tmdb_id', 'Movie', ['tmdb_id'], unique=False)
    op.create_table('user_watch_later',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('movie_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['Movie.id'], name='user_watch_later_movie_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], name='user_watch_later_user_id_fkey')
    )
    op.create_table('experience_screening_formats',
    sa.Column('cinema_experience_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('screening_format_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['cinema_experience_id'], ['CinemaExperience.id'], name='experience_screening_formats_cinema_experience_id_fkey'),
    sa.ForeignKeyConstraint(['screening_format_id'], ['ScreeningFormat.id'], name='experience_screening_formats_screening_format_id_fkey')
    )
    op.create_table('CinemaExperience',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"CinemaExperience_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('cinema_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('image_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['cinema_id'], ['Cinema.id'], name='CinemaExperience_cinema_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='CinemaExperience_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('CouponSaleCatalog',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"CouponSaleCatalog_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('cinema_experience_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('screening_resolution_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('screening_format_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('presentation_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ticket_class_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ticket_time_frame_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('price', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('original_price', sa.REAL(), autoincrement=False, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('expires_in', postgresql.INTERVAL(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['cinema_experience_id'], ['CinemaExperience.id'], name='CouponSaleCatalog_cinema_experience_id_fkey'),
    sa.ForeignKeyConstraint(['presentation_type_id'], ['PresentationType.id'], name='CouponSaleCatalog_presentation_type_id_fkey'),
    sa.ForeignKeyConstraint(['screening_format_id'], ['ScreeningFormat.id'], name='CouponSaleCatalog_screening_format_id_fkey'),
    sa.ForeignKeyConstraint(['screening_resolution_id'], ['ScreeningResolution.id'], name='CouponSaleCatalog_screening_resolution_id_fkey'),
    sa.ForeignKeyConstraint(['ticket_class_id'], ['TicketClass.id'], name='CouponSaleCatalog_ticket_class_id_fkey'),
    sa.ForeignKeyConstraint(['ticket_time_frame_id'], ['TicketTimeFrame.id'], name='CouponSaleCatalog_ticket_time_frame_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='CouponSaleCatalog_pkey')
    )
    op.create_table('Cinema',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Cinema_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('adderss', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('logo_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('backdrop_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('location_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('about', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('number_of_halls', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('usher_redeem_password', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Cinema_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('Admin',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Admin_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=60), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='Admin_pkey'),
    sa.UniqueConstraint('username', name='Admin_username_key')
    )
    op.create_table('CinemaReview',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"CinemaReview_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('cinema_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('rating', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('review', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['cinema_id'], ['Cinema.id'], name='CinemaReview_cinema_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], name='CinemaReview_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='CinemaReview_pkey')
    )
    op.create_table('CouponPurchase',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"CouponPurchase_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('amount_cents', sa.REAL(), autoincrement=False, nullable=True),
    sa.Column('payment_url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('transaction_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_paid', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('purchased_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], name='CouponPurchase_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='CouponPurchase_pkey'),
    sa.UniqueConstraint('transaction_id', name='CouponPurchase_transaction_id_key'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_CouponPurchase_order_id', 'CouponPurchase', ['order_id'], unique=False)
    op.create_table('ScheduledMovie',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"ScheduledMovie_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('movie_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('cinema_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['cinema_id'], ['Cinema.id'], name='ScheduledMovie_cinema_id_fkey'),
    sa.ForeignKeyConstraint(['movie_id'], ['Movie.id'], name='ScheduledMovie_movie_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='ScheduledMovie_pkey')
    )
    op.create_table('user_favourites',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('movie_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['Movie.id'], name='user_favourites_movie_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], name='user_favourites_user_id_fkey')
    )
    op.create_table('Faq',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Faq_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('question', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('answer', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='Faq_pkey')
    )
    op.create_table('InquiryTopic',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"InquiryTopic_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='InquiryTopic_pkey')
    )
    op.create_table('user_followers',
    sa.Column('follower_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('following_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['follower_id'], ['User.id'], name='user_followers_follower_id_fkey'),
    sa.ForeignKeyConstraint(['following_id'], ['User.id'], name='user_followers_following_id_fkey')
    )
    op.create_table('PromoCodeUse',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"PromoCodeUse_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('promo_code_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('coupon_purchase_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['coupon_purchase_id'], ['CouponPurchase.id'], name='PromoCodeUse_coupon_purchase_id_fkey'),
    sa.ForeignKeyConstraint(['promo_code_id'], ['PromoCode.id'], name='PromoCodeUse_promo_code_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], name='PromoCodeUse_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='PromoCodeUse_pkey')
    )
    op.create_table('experience_presentation_types',
    sa.Column('cinema_experience_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('presentation_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['cinema_experience_id'], ['CinemaExperience.id'], name='experience_presentation_types_cinema_experience_id_fkey'),
    sa.ForeignKeyConstraint(['presentation_type_id'], ['PresentationType.id'], name='experience_presentation_types_presentation_type_id_fkey')
    )
    op.create_table('User',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"User_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('auth0_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('date_of_birth', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('profile_picture', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='User_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('MovieReview',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"MovieReview_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('movie_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_spoiler', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('rating', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('review', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['Movie.id'], name='MovieReview_movie_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], name='MovieReview_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='MovieReview_pkey')
    )
    op.create_table('Auth0Identity',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Auth0Identity_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('auth0_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('connection', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('provider', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('is_social', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['User.id'], name='Auth0Identity_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='Auth0Identity_pkey')
    )
    op.create_table('ScreeningFormat',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"ScreeningFormat_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='ScreeningFormat_pkey')
    )
    op.create_table('TicketClass',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"TicketClass_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='TicketClass_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('ScreeningResolution',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"ScreeningResolution_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='ScreeningResolution_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('experience_screening_resolutions',
    sa.Column('cinema_experience_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('screening_resolution_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['cinema_experience_id'], ['CinemaExperience.id'], name='experience_screening_resolutions_cinema_experience_id_fkey'),
    sa.ForeignKeyConstraint(['screening_resolution_id'], ['ScreeningResolution.id'], name='experience_screening_resolutions_screening_resolution_id_fkey')
    )
    op.create_table('movie_genres',
    sa.Column('movie_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('genre_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['genre_id'], ['Genre.id'], name='movie_genres_genre_id_fkey'),
    sa.ForeignKeyConstraint(['movie_id'], ['Movie.id'], name='movie_genres_movie_id_fkey')
    )
    op.create_table('PresentationType',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"PresentationType_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='PresentationType_pkey')
    )
    op.create_table('experience_ticket_classes',
    sa.Column('cinema_experience_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('ticket_class_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['cinema_experience_id'], ['CinemaExperience.id'], name='experience_ticket_classes_cinema_experience_id_fkey'),
    sa.ForeignKeyConstraint(['ticket_class_id'], ['TicketClass.id'], name='experience_ticket_classes_ticket_class_id_fkey')
    )
    op.create_table('TicketTimeFrame',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"TicketTimeFrame_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('from_time', postgresql.TIME(), autoincrement=False, nullable=False),
    sa.Column('to_time', postgresql.TIME(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='TicketTimeFrame_pkey')
    )
    op.drop_table('validator')
    # ### end Alembic commands ###
